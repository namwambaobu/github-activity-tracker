import httpx

from .command import SyncUserActivityCommand
from .schemas import GitHubEventSchema


async def handle_sync_user_activity(
    command: SyncUserActivityCommand,
    client: httpx.AsyncClient | None = None,
) -> list[GitHubEventSchema]:
    url = f"https://api.github.com/users/{command.username}/events"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    raw_json = response.json()


    return [GitHubEventSchema.model_validate(item) for item in raw_json]