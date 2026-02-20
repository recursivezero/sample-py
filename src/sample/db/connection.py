import io
from datetime import datetime

from utils.constants import MONGO_CONFIG

_mongo_client = None
_db = None


def connect_db():
    """
    Connect to MongoDB and return the Database object.
    Requires pymongo to be installed via the 'mongo' extra.
    """
    global _mongo_client, _db

    if _db is not None:
        return _db

    try:
        from pymongo import MongoClient
    except ImportError as e:
        raise RuntimeError(
            "Mongo support not installed. "
            "Install with: pip install sample[mongo] or poetry install --extras 'mongo'"
        ) from e

    try:
        uri = MONGO_CONFIG["MONGODB_URI"]
        name = MONGO_CONFIG["DATABASE_NAME"]
        print("Mongo URI =", repr(uri))

        _mongo_client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        # Force an actual connection attempt
        _mongo_client.admin.command("ping")
        _db = _mongo_client[name]
        print("MongoDB connected successfully.")
        return _db

    except KeyError as e:
        raise RuntimeError(f"MongoDB Configuration Error: Missing key {e}")

    except Exception as e:
        raise RuntimeError(f"MongoDB Connection Error: {e}")


def save_to_mongodb(data, collection):
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
