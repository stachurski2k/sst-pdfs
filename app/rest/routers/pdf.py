from fastapi import APIRouter, Query, Depends, BackgroundTasks
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form,Response,status
from typing import Dict, Any, Optional,List
from fastapi.responses import FileResponse
import uuid,shutil,sys,os
from fastapi import status
from application.exceptions import *
from ..schemas.pdf_request import PDFRequest
from dependencies import *

router = APIRouter()

@router.post("/generate-pdf-file")
def generate_pdf_file(
    pdfreq: PDFRequest,
    tasks:BackgroundTasks,
    pdf_service = Depends(get_pdf_service),
    mapper = Depends(get_rest_chart_mapper), 
    temp = Depends(get_temp_service),
    ):

    tmpath = temp.get_random_temp_filepath(extension="pdf")
    try:
        model = mapper.map_to_pdfdata(pdfreq)
        pdf_service.generate_to_file(model,tmpath)

        return FileResponse(tmpath, media_type="application/pdf", filename="pdf.pdf")

    except ChartParsingError as e:
        raise HTTPException(status_code=400,detail=f"{e}")

    except IncorrectChartType as e:
        raise HTTPException(status_code=400,detail=f"{e}")

    except ChartStrategyNotFound as e:
        raise HTTPException(status_code=400,detail=f"{e}")
    
    except TemplateNotFoundError as e:
        raise HTTPException(status_code=400,detail="Template was not found!")

    except ThemeNotFoundError as e:
        raise HTTPException(status_code=400,detail="Theme was not found!")

    except Exception as e:
        raise HTTPException(status_code=500,detail=f"{e}")

    finally:

        tasks.add_task(temp.remove_temp_file,tmpath)