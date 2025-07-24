from typing import Literal, List, Dict,Union
from pydantic import BaseModel

class ChartConfig(BaseModel):
    title: str
    xAxis: str
    yAxis: str
    width: float #in pixels
    height: float #in pixels

class Series(BaseModel):
    x: List[float]
    y: List[float]

class LineChart(BaseModel):
    config: ChartConfig
    series: Dict[str,Series]

class BarChart(BaseModel):
    config: ChartConfig
    series: Series

class HistogramChart(BaseModel):
    config: ChartConfig
    data: List[float]

Chart = Union[
    LineChart,
    BarChart,
    HistogramChart
]