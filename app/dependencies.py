import logging 
from core.config import settings
import os
from datetime import datetime
from functools import lru_cache

@lru_cache()
def get_logger()-> logging.Logger:
    os.makedirs(settings.LOGS_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(settings.LOGS_DIR, f"log_{timestamp}.log")

    logging.basicConfig(
        format="%(levelname)s | %(asctime)s | %(message)s | %(pathname)s | %(lineno)d",
        filename=log_file
    )

    logger = logging.getLogger("global_logger")
    
    log_level=getattr(logging, settings.LOG_LEVEL.upper())
    logger.setLevel(log_level)

    return logger