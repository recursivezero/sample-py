from datetime import datetime
from typing import Optional
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
import io
from utils.constants import MONGO_CONFIG

mongo_client: Optional[MongoClient]
db: Optional[Database]
collection: Optional[Collection]
fabric_collection: Optional[Collection]
processing_times_collection: Optional[Collection]

# Initialize MongoDB connections with error handling
try:
    mongo_client = MongoClient(MONGO_CONFIG["MONGODB_URI"])
    db = mongo_client[MONGO_CONFIG["DATABASE_NAME"]]
except KeyError as e:
    print(f"MongoDB Configuration Error: Missing key {e}")
    mongo_client = None
    db = None
    collection = None

except Exception as e:
    print(f"MongoDB Connection Error: {e}")
    mongo_client = None
    db = None


def save_to_mongodb(data: dict, collection):
    """Insert processed JSON data into MongoDB"""
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