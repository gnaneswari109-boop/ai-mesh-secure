from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ai-mesh-secure"
    redis_url: str = "redis://localhost:6379/0"
    database_url: str = "sqlite:///./ai_mesh.db"
    debug: bool = True
    openai_api_key: str = ""
    gemini_api_key: str = ""

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
