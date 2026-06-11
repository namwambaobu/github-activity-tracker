from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, String, Integer, func
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from src.database.base import Base  # ← correct import direction



class GitHubEvent(Base):
    __tablename__ = "github_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(String(100), index=True)
    event_type: Mapped[str] = mapped_column(String(100), index=True)
    event_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    repo_name: Mapped[str] = mapped_column(String(255), index=True)


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        index=True
    )

    payload: Mapped[dict] = mapped_column(JSONB)