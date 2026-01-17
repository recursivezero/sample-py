import logging
from contextlib import asynccontextmanager
from pathlib import Path

from db.connection import connect_db
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.constants import PORT

from . import __version__


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("🏷️ Sample version:", __version__)
    logging.info("Starting FastAPI server...")
    try:
        db = connect_db()
        print(f"Using database: {db.name}")
    except Exception as e:
        logging.error(f"⚠️ Database connection failed: {e}")
    print("App is ready.")

    yield  # <-- control passes to request handling

    # Shutdown logic
    logging.info("Shutting down FastAPI server...")
    # If you want to close DB connections, do it here


# Create FastAPI app with lifespan handler
app = FastAPI(lifespan=lifespan)

# Mount assets and pages
app.mount("/static", StaticFiles(directory="assets"), name="static")

# Point Jinja2 to your templates directory
templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parents[2] / "templates")
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the main index.html at root."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})


templates = Jinja2Templates(directory="templates")


@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, full_path: str):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)


def main():
    """Entry point for CLI dev command."""
    import uvicorn

    uvicorn.run("sample.__main__:app", host="127.0.0.1", port=PORT, reload=True)


if __name__ == "__main__":
    main()
