from typing import Literal, List, Dict,Union, Annotated
from pydantic import BaseModel, model_validator ,Field
from rest.exceptions import *


class ChartConfigRequest(BaseModel):
    title: str
    xAxis: str
    yAxis: str
    width: float #in pixels
    height: float #in pixels

class SeriesReqest(BaseModel):
    x: List[float]
    y: List[float]

class LineChartRequest(BaseModel):
    chartType:Literal["line"]
    series: Dict[str,SeriesReqest]
    config: ChartConfigRequest

    @model_validator(mode="before")
    def validate_lengths(cls, values):
        series = values.get('series')
        print(series)
        if any(len(ser["x"]) != len(ser["y"]) for label, ser in series.items()):
            raise ChartParsingError()
        return values

class HistogramRequest(BaseModel):
    chartType:Literal["hist"]
    data: List[float]
    config: ChartConfigRequest


ChartRequest = Annotated[
    Union[LineChartRequest,HistogramRequest],
    Field(discriminator="chartType")
]
