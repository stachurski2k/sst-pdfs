from fastapi import APIRouter, Query, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form,Depends
from fastapi.responses import FileResponse
from typing import Dict, Any, Optional,List
from rest.schemas.chart_request import *
import uuid,shutil,sys,os
from dependencies import get_chart_strategy_factory, get_rest_chart_mapper, get_temp_service


router = APIRouter()

@router.post("/generate-chart-file")
def generate_chart_file(
    chart: ChartRequest,
    tasks:BackgroundTasks,
    chart_strategy_factory = Depends(get_chart_strategy_factory),
    mapper = Depends(get_rest_chart_mapper), 
    temp = Depends(get_temp_service),
    ):

    tmpath = temp.get_random_temp_filepath(extension="png")
    try:
        model = mapper.map_to_model(chart)
        chart_strategy_factory.generate_to_file(model,tmpath)

        return FileResponse(tmpath, media_type="image/png", filename="chart.png")

    except Exception as e:
        raise

    finally:

        tasks.add_task(temp.remove_temp_file,tmpath)


