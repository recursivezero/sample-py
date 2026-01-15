import logging
import os
from pathlib import Path

from dotenv import load_dotenv

APP_TITLE = ":blue[Greeting Feature]"
DEFAULT_GREETING = "Hello"
FAQ_TITLE = "FAQs"
PORT = 8000
# --- Asset paths ---
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
ASSETS_DIR = PROJECT_ROOT / "assets" / "images"
COMPANY_LOGO = ASSETS_DIR / "logo.png"

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


def safe_get(secret_path: str, env_key: str = "", default: str = "") -> str:
    value = default
    source = "default"

    if source != "secrets" and env_key:
        env_val = os.getenv(env_key)

        if env_val is not None:
            env_val = env_val.strip().strip('"').strip("'")

            if env_val:
                value = env_val
                source = "env"

    logging.info(
        f"Loaded config for '{env_key or secret_path}' from [{source}]",
        extra={"color": "yellow"},
    )
    return value


MONGODB_URI = safe_get("mongodb.MONGODB_URI", "MONGODB_URI")
DATABASE_NAME = safe_get("mongodb.DATABASE_NAME", "DATABASE_NAME")

print("MongoDB URI:", MONGODB_URI)
print("Database Name:", DATABASE_NAME)

MONGO_CONFIG = {
    "MONGODB_URI": MONGODB_URI,
    "DATABASE_NAME": DATABASE_NAME,
}
