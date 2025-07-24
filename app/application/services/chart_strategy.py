from abc import ABC, abstractmethod
from typing import Dict, Any
from fastapi.responses import StreamingResponse
from domain.value_objects.charts import *

class ChartStrategy(ABC):
    @abstractmethod
    def generate_to_file(self,chart: Chart, output_path:str):
        pass