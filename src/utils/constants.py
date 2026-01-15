import os
from pathlib import Path
import logging
from dotenv import load_dotenv

load_dotenv()


APP_TITLE = ":blue[Greeting Feature]"
DEFAULT_GREETING = "Hello"
FAQ_TITLE = "FAQs"
PORT = 8000
# --- Asset paths ---
PROJECT_ROOT = Path(__file__).parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets" / "images"
COMPANY_LOGO = ASSETS_DIR / "logo.png"

def safe_get(env_key: str) -> str:
    value = os.getenv(env_key)

    if not value:
        raise RuntimeError(f"Missing required environment variable: {env_key}")

    logging.info(f"Loaded config '{env_key}' from [env]")
    return value

MONGODB_URI = safe_get("MONGODB_URI")
DATABASE_NAME = safe_get("DATABASE_NAME")

print("MongoDB URI:", MONGODB_URI)
print("Database Name:", DATABASE_NAME)

MONGO_CONFIG = {
    "MONGODB_URI": MONGODB_URI,
    "DATABASE_NAME": DATABASE_NAME,
}
