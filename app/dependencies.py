import logging 
from config import settings
import os
from datetime import datetime
from functools import lru_cache
from services.chart_strategy_factory import ChartStrategyFactory
from services.temp_service import TempService
from rest.mappers.chart_mapper import *

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


@lru_cache
def get_chart_strategy_factory():
    return ChartStrategyFactory(get_logger())

@lru_cache
def get_rest_chart_mapper():
    return ChartMapper(get_logger())

@lru_cache
def get_temp_service():
    return TempService(get_logger(),settings.TEMP_DIR)