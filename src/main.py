from fastapi import FastAPI

from src.config import settings

app = FastAPI(

    title= "Github Activity Tracker"
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "env" : settings.app_env
    }