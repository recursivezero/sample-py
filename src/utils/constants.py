import logging
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# These should be in environment variables or .env file.
DEFAULT_PORT = 8005
DEFAULT_API_PREFIX = "/api/v1"
DEFAULT_MONGODB_URI = (
    "mongodb://127.0.0.1:27017/?retryWrites=true&w=majority&appName=Sample"
)
DEFAULT_DATABASE_NAME = "sample_db"

GREETING = "Hello"

# --- Asset paths ---
PROJECT_ROOT = Path(__file__).parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets" / "images"
COMPANY_LOGO = ASSETS_DIR / "logo.png"


def safe_get(env_key: str, default) -> str:
    value = os.getenv(env_key, default)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {env_key}")

    logging.info(f"Loaded config '{env_key}' from [env]")
    return value


MONGODB_URI = safe_get("MONGODB_URI", DEFAULT_MONGODB_URI)
DATABASE_NAME = safe_get("DATABASE_NAME", DEFAULT_DATABASE_NAME)
API_PREFIX = safe_get("API_PREFIX", DEFAULT_API_PREFIX)
PORT = int(safe_get("PORT", DEFAULT_PORT))

print("MongoDB URI:", MONGODB_URI)
print("Database Name:", DATABASE_NAME)

MONGO_CONFIG = {
    "MONGODB_URI": MONGODB_URI,
    "DATABASE_NAME": DATABASE_NAME,
}
