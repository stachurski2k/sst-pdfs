from rest.schemas.chart_request import *
from rest.schemas.pdf_request import *
from domain.value_objects.charts import *
from domain.value_objects.pdfs import *
from rest.exceptions import *

class ChartMapper():
    def __init__(self,log):
        self.log=log
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
    
    def map_to_pdfdata(self,req: PDFRequest):

        return PDFData(
            template_name=req.template_name,
            theme_name=req.theme_name,
            params=req.params
        )
