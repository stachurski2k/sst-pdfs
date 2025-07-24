from .charts import router as chart_router

def register_routes(app):
    app.include_router(chart_router,prefix="/api")



