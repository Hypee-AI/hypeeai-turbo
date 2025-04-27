from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Backend"
    api_version: str = "v1"

    class Config:
        env_file = ".env"  # Support for environment variables

settings = Settings()
