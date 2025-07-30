from .chart_strategy_factory import *
from domain.value_objects.charts import *
from ...exceptions import *
from .line_chart_strategy import *
from .histogram_strategy import *

class ChartStrategyFactory():
    
    def __init__(self,log):
        """
        Initializes the ChartStrategyFactory.

        Args:
            log:  The logger to use for logging.
        """
        self.log=log

    def generate_to_file(self,chart: Chart,output_path: str):
        """
        Generates a chart to a file using the appropriate strategy.

        Args:
            chart (Chart): The chart data to generate.
            output_path (str): The path to save the generated chart file.

        Returns:
            None

        Raises:
            ChartStrategyNotFound: If no strategy is found for the chart type.
        """
        if isinstance(chart, LineChart):
            LineChartStrategy().generate_to_file(chart,output_path)
            return

        if isinstance(chart, HistogramChart):
            HistogramStrategy().generate_to_file(chart,output_path)
            return

        self.log.error(f"Chart strategy not found for {chart}")
        raise ChartStrategyNotFound()