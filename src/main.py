from fastapi import FastAPI

from src.github.features.sync_user_activity.command import (
    SyncUserActivityCommand,
)
from src.github.features.sync_user_activity.handler import (
    handle_sync_user_activity,
)

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/users/{username}/sync")
async def sync_user_activity(username: str):
    command = SyncUserActivityCommand(username=username)

    events = await handle_sync_user_activity(command)

    return events


# @router.post("/users/{username}/sync")
# async def sync_user_activity(
#     username: str,
#     client: httpx.AsyncClient = Depends(get_http_client),
# ):
#     command = SyncUserActivityCommand(username=username)
#     events = await handle_sync_user_activity(command, client)
#     return events