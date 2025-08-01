from typing import Literal, List, Dict,Union, Any
from pydantic import BaseModel

class PDFData(BaseModel):
    template_name:str
    theme_name:str
    params: Dict[str,Any]
    
