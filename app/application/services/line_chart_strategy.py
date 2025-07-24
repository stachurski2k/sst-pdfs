from .chart_strategy import *
from domain.value_objects.charts import *
from ..exceptions import *
import matplotlib.pyplot as plt

class LineChartStrategy(ChartStrategy):
    def generate_to_file(self,chart:Chart, output_path:str):

        if not isinstance(chart, LineChart):

            raise IncorrectChartType()

        config = chart.config
        plt.figure(figsize=(config.width/100,config.height/100))

        for label, series in chart.series.items():
            plt.plot(series.x,series.y,label=label)

        plt.xlabel(config.xAxis)
        plt.ylabel(config.yAxis)
        plt.title(config.title)

        plt.savefig(output_path)
        plt.close()

        

        