from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

web_router = APIRouter()

templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parents[3] / "templates")
)


@web_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@web_router.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})


@web_router.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, full_path: str):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
