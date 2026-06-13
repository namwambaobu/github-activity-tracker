from dataclasses import dataclass


@dataclass(frozen=True)
class SyncUserActivityCommand:
    username: str