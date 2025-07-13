from datetime import timedelta

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TITLE: str = "Restaurant Order Management API"
    JWT_SECRET_KEY: str = "VERY-SECRET-JTW-KEY"
    JWT_EXPIRES_IN: timedelta = timedelta(seconds=3600)
    JWT_ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings() # type: ignore


