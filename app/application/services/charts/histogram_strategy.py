from .chart_strategy import *
from domain.value_objects.charts import *
from ...exceptions import *
import matplotlib.pyplot as plt

class HistogramStrategy(ChartStrategy):
    
    def generate_to_file(self,chart:Chart, output_path:str):
        """
        Generates a histogram chart to a file.

        Args:
            chart (Chart): The chart data to generate. Must be a HistogramChart.
            output_path (str): The path to save the generated chart file.

        Returns:
            None

        Raises:
            IncorrectChartType: If the chart is not a HistogramChart.
        """
        if not isinstance(chart, HistogramChart):

            raise IncorrectChartType(f"Expected : HistogramChart but got: {type(chart)}")

        config = chart.config
        plt.figure(figsize=(config.width/100,config.height/100))

        plt.hist(chart.data)

        plt.xlabel(config.xAxis)
        plt.ylabel(config.yAxis)
        plt.title(config.title)

        plt.savefig(output_path)
        plt.close()

        

        
