import io
from datetime import datetime
from typing import Optional

from pymongo import MongoClient
from pymongo.database import Database
from utils.constants import MONGO_CONFIG

_mongo_client: Optional[MongoClient] = None
_db: Optional[Database] = None


def connect_db() -> Database:
    global _mongo_client, _db

    if _db is not None:
        return _db

    try:
        uri = MONGO_CONFIG["MONGODB_URI"]
        name = MONGO_CONFIG["DATABASE_NAME"]
        print("Mongo URI =", repr(uri))

        _mongo_client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        # This forces an actual connection attempt
        _mongo_client.admin.command("ping")
        _db = _mongo_client[name]
        print("MongoDB connected successfully.")
        return _db

    except KeyError as e:
        raise RuntimeError(f"MongoDB Configuration Error: Missing key {e}")

    except Exception as e:
        raise RuntimeError(f"MongoDB Connection Error: {e}")


def save_to_mongodb(data: dict, collection):
    try:
        data["created_at"] = datetime.now()
        result = collection.insert_one(data)
        return result.inserted_id
    except Exception as e:
        print("MongoDB Insert Error:", e)
        return False


def pil_to_bytes(pil_image):
    buf = io.BytesIO()
    pil_image.save(buf, format="PNG")
    buf.seek(0)
    return buf
