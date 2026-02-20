from fastapi import APIRouter, FastAPI, HTTPException, Request
from pydantic import BaseModel
from sample.utils.constants import API_PREFIX, GREETING, PORT
from sample.utils.helper import normalize_name
from starlette.responses import HTMLResponse, JSONResponse
from sample import __version__

app = FastAPI(
    title="Sample API",
    version=__version__,
)

api_router = APIRouter()
greet_router = APIRouter(prefix=API_PREFIX, tags=["V1"])


class GreetRequest(BaseModel):
    name: str


class GreetResponse(BaseModel):
    message: str


@api_router.get("/health")
def health_check():
    return {"status": "ok"}


@greet_router.post("/greet", response_model=GreetResponse)
def greet_user(payload: GreetRequest):
    clean_name = normalize_name(payload.name)

    if not clean_name:
        raise HTTPException(status_code=400, detail="Invalid name provided")

    return {"message": f"{GREETING}, {clean_name} 👋"}


@api_router.get("/version", tags=["Version"])
def version():
    return {"version": api_router.version}


@api_router.get("/", response_class=HTMLResponse, tags=["Home"])
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


@api_router.get("/help", tags=["Help"])
def get_help():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to the Sample BoilerPlate API! Visit /docs for API documentation."
        },
    )


app.include_router(api_router)
app.include_router(greet_router)


def start():
    import uvicorn

    uvicorn.run("sample.api.routes:app", host="127.0.0.1", port=PORT, reload=True)
