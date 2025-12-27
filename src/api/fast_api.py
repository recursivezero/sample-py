from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from . import __version__
from utils.constants import DEFAULT_GREETING
from utils.helper import normalize_name

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


class GreetRequest(BaseModel):
    name: str


class GreetResponse(BaseModel):
    message: str


@app.get("/version")
def version():
    return {"version": app.version}


@app.get("/", response_class=HTMLResponse)
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


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/greet", response_model=GreetResponse)
def greet_user(payload: GreetRequest):
    clean_name = normalize_name(payload.name)

    if not clean_name:
        raise HTTPException(status_code=400, detail="Invalid name provided")

    return {"message": f"{DEFAULT_GREETING}, {clean_name} 👋"}


def start():
    import uvicorn

    print(f"🧵 {__version__}\n")
    uvicorn.run("api.fast_api:app", host="127.0.0.1", port=5000, reload=True)


if __name__ == "__main__":
    start()
