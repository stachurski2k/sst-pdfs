from abc import ABC, abstractmethod
from typing import Dict, Any
from fastapi.responses import StreamingResponse
from domain.value_objects.charts import *

class ChartStrategy(ABC):
    @abstractmethod
    def generate_to_file(self, chart: Chart, output_path: str):
        """
        Generates a chart to a file.

        Args:
            chart (Chart): The chart data to generate.
            output_path (str): The path to save the generated chart file.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented by a concrete class.
        """
        pass