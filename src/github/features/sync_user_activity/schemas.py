from datetime import datetime
from typing import Any

from pydantic import BaseModel


class RepoSchema(BaseModel):
    name: str


class GitHubEventSchema(BaseModel):
    id: str
    type: str
    repo: RepoSchema
    created_at: datetime
    payload: dict[str, Any]