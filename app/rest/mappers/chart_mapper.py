from rest.schemas.chart_request import *
from domain.value_objects.charts import *
from rest.exceptions import *

class ChartMapper():
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
        
        raise ChartMappingError()
