from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    cors_origins: List[str] = ["*"]
    cors_methods: List[str] = ["*"]
    cors_headers: List[str] = ["*"]
    cors_allow_credentials: bool = True
    rate_limit_per_minute: int = 100
    project_name: str = "My FastAPI Project"
    project_description: str = "API description"
    project_version: str = "1.0.0"
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str
    skip_auth: List[str] = []
    secret_key: str
    algorithm: str = "HS256"
    enable_logging: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
