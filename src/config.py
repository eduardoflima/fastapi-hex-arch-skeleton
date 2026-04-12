from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    first_id: int

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


def get_settings() -> Settings:
    return Settings()
