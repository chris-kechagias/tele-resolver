from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    telegram_bot_token: str
    chatbot_api_url: str = "http://localhost:8000"
    database_url: str = "sqlite:///./tele_resolver.db"


config = Config()
