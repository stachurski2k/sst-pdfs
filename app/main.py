from fastapi import FastAPI
from core.config import settings
from api.routers.register_routers import register_routes
from dependencies import get_logger


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

@app.get("/")
def root():
    return "App is running!"

register_routes(app)

logger = get_logger()
logger = get_logger()
logger = get_logger()
logger.info("APP STARTING")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=settings.PORT)