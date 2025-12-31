import os
from pathlib import Path
from typing import Any
import streamlit as st
import logging



APP_TITLE = ":blue[Greeting Feature]"
DEFAULT_GREETING = "Hello"
FAQ_TITLE = "FAQs"

# --- Asset paths ---
PROJECT_ROOT = Path(__file__).parent.parent
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
    secrets_file = Path(".streamlit/secrets.toml")

    # Only try accessing secrets if the file exists
    if secrets_file.exists():
        try:
            secrets_dict: dict[str, Any] = dict(st.secrets)  # Convert to plain dict
            val = secrets_dict

            for key in secret_path.split("."):
                val = (
                    val.get(key, {}) if isinstance(val, dict) else getattr(val, key, {})
                )
            if val and val != {}:
                value = str(val)
                source = "secrets"
        except Exception as e:
            logging.debug(f"Could not retrieve secret '{secret_path}': {e}")

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

MONGODB_URI = safe_get("mongodb.MONGODB_URI", "MONGODB_URI")
DATABASE_NAME = safe_get("mongodb.DATABASE_NAME", "DATABASE_NAME")

MONGO_CONFIG = {
    "MONGODB_URI": MONGODB_URI,
    "DATABASE_NAME": DATABASE_NAME,
}