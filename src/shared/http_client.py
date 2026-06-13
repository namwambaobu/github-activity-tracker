import httpx
from typing import AsyncGenerator

async def get_http_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(
        headers={"Accept": "application/vnd.github+json"},
        timeout=10.0,
    ) as client:
        yield client