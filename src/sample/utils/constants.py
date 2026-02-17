import logging
import os
from pathlib import Path

from sample.utils.config import load_env

load_env()
APP_TITLE = ":blue[Greeting Feature]"
DEFAULT_GREETING = "Hello"
FAQ_TITLE = "FAQs"
logging.basicConfig(
    level=logging.INFO,  # or DEBUG
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# --- Asset paths ---
PROJECT_ROOT = Path(__file__).parents[2]
ASSETS_DIR = PROJECT_ROOT / "assets" / "images"
COMPANY_LOGO = ASSETS_DIR / "logo.png"


def safe_get(secret_path: str, env_key: str = "", default: str = "") -> str:
    """
    Safely retrieve a configuration value from:
    1. Streamlit secrets (if secrets.toml exists)
    2. Environment variable
    3. Default fallback

    Logs the source used for each config value.
    """
    value = default
    source = "default"

    # If secrets not used, fallback to env
    if source != "secrets" and env_key:
        env_val = os.getenv(env_key)
        if env_val:
            value = env_val
            source = "env"

    logging.info(
        f"Loaded config for '{env_key or secret_path}' from [{source}]",
        extra={"color": "yellow"},
    )
    return value


def get_mongo_config():
    return {
        "MONGODB_URI": safe_get("mongodb.MONGODB_URI", "MONGODB_URI"),
        "DATABASE_NAME": safe_get("mongodb.DATABASE_NAME", "DATABASE_NAME"),
    }


MONGO_CONFIG = get_mongo_config()
# === Environment Selection ===
ENVIRONMENT = safe_get("env.ENVIRONMENT", "ENVIRONMENT", "development").lower()
logging.info(f"Environment: {ENVIRONMENT}", extra={"color": "yellow"})
logging.info(f"Project root: {PROJECT_ROOT}", extra={"color": "yellow"})
