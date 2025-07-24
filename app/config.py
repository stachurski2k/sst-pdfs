from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Sample APP"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    PORT:int = 23000
    LOGS_DIR:str ="logs"
    LOG_LEVEL:str ="DEBUG"

settings = Settings()