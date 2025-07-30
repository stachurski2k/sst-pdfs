from .charts import router as chart_router
from .templates import router as templats_router
from .pdf import router as pdf_router
from .themes import router as themes_router
from .images import router as images_router

def register_routes(app):
    app.include_router(chart_router,prefix="/api",tags=["Charts"])
    app.include_router(templats_router,prefix="/api/templates",tags=["Templates"])
    app.include_router(themes_router,prefix="/api/themes",tags=["Themes"])
    app.include_router(images_router,prefix="/api/imgs",tags=["Images"])
    app.include_router(pdf_router,prefix="/api/pdf",tags=["PDF"])



