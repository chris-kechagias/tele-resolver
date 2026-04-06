from sqlmodel import SQLModel, create_engine

from app.core.config import config

engine = create_engine(config.database_url)


def init_db() -> None:
    """Create all tables on startup."""
    SQLModel.metadata.create_all(engine)
