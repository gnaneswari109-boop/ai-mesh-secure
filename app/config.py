from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "ai-mesh-secure"
    redis_url: str = "redis://localhost:6379/0"
    database_url: str = "sqlite:///./ai_mesh.db"
    debug: bool = True

settings = Settings()
