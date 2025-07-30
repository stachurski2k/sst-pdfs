from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Sample APP"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    PORT:int = 23000
    LOGS_DIR:str ="logs"
    LOG_LEVEL:str ="DEBUG"
    TEMP_DIR:str = "tmp"
    THEMES_DIR:str = "static/css"
    TEMPLATES_DIR:str = "static/templates"
    IMAGES_DIR:str = "static/img"
    USE_REST:bool = True
    USE_GRPC:bool = True
    REST_PORT:int = 23000
    GRPC_PORT:int = 23001

settings = Settings()