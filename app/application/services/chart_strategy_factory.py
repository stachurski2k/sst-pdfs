from .chart_strategy_factory import *
from domain.value_objects.charts import *
from ..exceptions import *
from .line_chart_strategy import *

class ChartStrategyFactory():
    def __init__(self,log):

        self.log=log

    def generate_to_file(self,chart: Chart,output_path: str):

        if isinstance(chart, LineChart):
            LineChartStrategy().generate_to_file(chart,output_path)
            return

        self.log.error(f"Chart strategy not found for {chart}")
        raise ChartStrategyNotFound()