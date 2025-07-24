
from typing import Literal, List, Dict,Union, Any
from pydantic import BaseModel

class PDFRequest(BaseModel):
    template_name:str
    theme_name:str
    params: Dict[str,Any]