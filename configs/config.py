from pydantic import BaseSettings


class Settings(BaseSettings):
    token: str
    admin_id: str

    class Config:
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = "utf-8"


settings = Settings()
