import logging 
from config import settings
import os
from datetime import datetime
from functools import lru_cache
from application.services.charts.chart_strategy_factory import ChartStrategyFactory
from application.services.temp_service import TempService
from application.repos.themes_repo import ThemesRepo
from application.repos.images_repo import ImagesRepo
from application.repos.templates_repo import TemplatesRepo
from application.services.pdf_service import PDFService
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

@lru_cache
def get_themes_repo():
    return ThemesRepo(get_logger(),settings.THEMES_DIR)

@lru_cache
def get_templates_repo():
    return TemplatesRepo(get_logger(),settings.TEMPLATES_DIR)

@lru_cache
def get_images_repo():
    return ImagesRepo(get_logger(),settings.IMAGES_DIR)

@lru_cache
def get_pdf_service():
    return PDFService(get_logger(),os.getcwd(),get_templates_repo(),get_themes_repo())