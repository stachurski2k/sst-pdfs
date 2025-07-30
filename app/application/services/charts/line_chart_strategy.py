from .chart_strategy import *
from domain.value_objects.charts import *
from ...exceptions import *
import matplotlib.pyplot as plt

class LineChartStrategy(ChartStrategy):
    def generate_to_file(self,chart:Chart, output_path:str):
        """
        Generates a line chart to a file.

        Args:
            chart (Chart): The chart data to generate. Must be a LineChart.
            output_path (str): The path to save the generated chart file.

        Returns:
            None

        Raises:
            IncorrectChartType: If the chart is not a LineChart.
        """
        if not isinstance(chart, LineChart):

            raise IncorrectChartType(f"Expected: LineChart, got: {type(chart)}")

        config = chart.config
        plt.figure(figsize=(config.width/100,config.height/100))

        for label, series in chart.series.items():
            plt.plot(series.x,series.y,label=label)

        plt.xlabel(config.xAxis)
        plt.ylabel(config.yAxis)
        plt.title(config.title)

        plt.savefig(output_path)
        plt.close()

        

        
