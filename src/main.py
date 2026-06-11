from fastapi import FastAPI

app = FastAPI(

    title= "Github Activity Tracker"
)


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }