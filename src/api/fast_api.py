from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from . import __version__
from utils.constants import DEFAULT_GREETING
from utils.helper import normalize_name
import streamlit as st

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

def apply_common_styles():
    st.markdown("""
        <style>
        .reportview-container {
            background: #f0f2f6;
        }
        footer {visibility: hidden;}
        .main-header {
            font-size: 2.5rem;
            color: #4B4B4B;
            text-align: center;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Sample Python App</div>', unsafe_allow_html=True)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content = {
            "status": "error",
            "message": "Invalid data provided",
            "details": exc.errors(),
        },
    )
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = {
            "status": "error",
            "message": "An internal server error occured",
            "details": str(exc),
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
    apply_common_styles()
    st.write("Welcome to the app!")
    start()
    
