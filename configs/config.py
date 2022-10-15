from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    ADMIN_ID: str
    LOGGER_LEVEL: str

    class Config:
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = "utf-8"


settings = Settings()
