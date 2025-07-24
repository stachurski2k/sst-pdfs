from .charts import router as chart_router
from .templates import router as templats_router
from .themes import router as themes_router

def register_routes(app):
    app.include_router(chart_router,prefix="/api")
    #app.include_router(templats_router,prefix="/api/templates")
    app.include_router(themes_router,prefix="/api/themes")



