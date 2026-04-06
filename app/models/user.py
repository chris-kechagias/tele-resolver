from typing import Optional

from sqlmodel import Field, SQLModel


class TelegramUser(SQLModel, table=True):
    """Stores per-user OpenAI API keys."""

    id: Optional[int] = Field(default=None, primary_key=True)
    telegram_id: int = Field(unique=True, index=True)
    openai_api_key: Optional[str] = Field(default=None)
