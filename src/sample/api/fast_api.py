from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from utils.constants import API_PREFIX, GREETING
from utils.helper import normalize_name

from . import __version__

app = FastAPI(
    title="sample API",
    description="API endpoints for Sample with rate limiting",
    version=__version__,
    redoc_url="/redoc",
    swagger_ui_parameters={
        "docExpansion": "none",  # Collapse all endpoints by default
        "defaultModelsExpandDepth": -1,  # Hide schemas section
        "displayRequestDuration": True,  # Show request duration
        "layout": "BaseLayout",  # Clean layout
        "syntaxHighlight": {"theme": "obsidian"},  # Dark theme
    },
)

api_v1 = APIRouter(
    prefix=API_PREFIX,
    tags=["V1"],
)


class GreetRequest(BaseModel):
    name: str


class GreetResponse(BaseModel):
    message: str


@app.get("/version", tags=["Version"])
def version():
    return {"version": app.version}


@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def read_root(request: Request):
    return """
    <html>
        <head>
            <title>🎉 Sample Api 🎉</title>
            <style>
                body {
                    background: linear-gradient(to right, #268387, #e3898a);
                    text-align: center;
                    padding-top: 10%;
                    color: #fff;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 0.2em;
                }
                p {
                    font-size: 1.2em;
                }
                a {
                    color: #fff;
                    background: #4CAF50;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 10px;
                    font-weight: bold;
                    transition: background 0.3s ease;
                }
                a:hover {
                    background: #45a049;
                }
            </style>
        </head>
        <body>
            <h1>🎈 This is sample API Tool 🎈</h1>
            <p>Explore the <a href="/docs">API Documentation</a></p>
        </body>
    </html>
    """


@app.get("/health", tags=["Help"])
def health_check():
    return {"status": "ok"}


@api_v1.get("/help", tags=["Help"])
def get_help():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to the Sample BoilerPlate API! Visit /docs for API documentation."
        },
    )


@api_v1.post("/greet", response_model=GreetResponse)
def greet_user(payload: GreetRequest):
    clean_name = normalize_name(payload.name)

    if not clean_name:
        raise HTTPException(status_code=400, detail="Invalid name provided")

    return {"message": f"{GREETING}, {clean_name} 👋"}


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        endpoint = request.url.path

        return JSONResponse(
            status_code=404,
            content={
                "error": f"Endpoint '{endpoint}' does not exist, use /docs to see available endpoints.",
                "status": 404,
            },
        )

    # fallback for other HTTP errors
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


# suppress chrome log
@app.get("/.well-known/appspecific/com.chrome.devtools.json")
async def chrome_devtools_probe():
    return JSONResponse({})


app.include_router(api_v1)


def start():
    import uvicorn

    print(f"🧵 {__version__}\n")
    uvicorn.run("api.fast_api:app", host="127.0.0.1", port=5000, reload=True)


if __name__ == "__main__":
    start()
