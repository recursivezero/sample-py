import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sample.api.routes import greet_router
from sample.api.web_page import web_router
from sample.db.connection import connect_db
from sample.utils.constants import PORT


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting FastAPI server...")
    try:
        db = connect_db()
        print(f"Using database: {db.name}")
    except Exception as e:
        logging.error(f"⚠️ Database connection failed: {e}")

    yield

    logging.info("Shutting down FastAPI server...")


app = FastAPI(
    title="Sample API",
    lifespan=lifespan,
)

# Static
app.mount("/static", StaticFiles(directory="assets"), name="static")

# Templates
templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parent / "templates")
)


app.include_router(web_router)
app.include_router(greet_router)


def start():
    import uvicorn

    uvicorn.run("sample.api.main:app", host="127.0.0.1", port=PORT, reload=True)
