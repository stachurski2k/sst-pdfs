from rest.schemas.chart_request import *
from rest.schemas.pdf_request import *
from domain.value_objects.charts import *
from domain.value_objects.pdfs import *
from rest.exceptions import *

class ChartMapper():
    def __init__(self,log,images_repo):
        self.log=log
        self.imgs=images_repo
        
    def map_to_model(self,request: ChartRequest):
        if isinstance(request,LineChartRequest):
            config = ChartConfig(
                title=request.config.title,
                xAxis=request.config.xAxis,
                yAxis=request.config.yAxis,
                width=request.config.width,
                height=request.config.height,
            )
            series = {
                key: Series(x=value.x, y=value.y)
                for key, value in request.series.items()
            }
            return LineChart(config=config, series=series)

        if isinstance(request,HistogramRequest):
            config = ChartConfig(
                title=request.config.title,
                xAxis=request.config.xAxis,
                yAxis=request.config.yAxis,
                width=request.config.width,
                height=request.config.height,
            )
            data=request.data
            return HistogramChart(config=config, data=data)
        
        raise ChartMappingError()
    
