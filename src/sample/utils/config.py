import os

from dotenv import load_dotenv


def load_env():
    env = os.getenv("ENV", "development")

    file_map = {
        "production": ".env.production",
        "development": ".env.development",
    }

    load_dotenv(file_map.get(env, ".env.development"), override=True)
    return env
