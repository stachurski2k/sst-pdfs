from fastapi import APIRouter, Query, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form,Depends
from fastapi.responses import FileResponse
from typing import Dict, Any, Optional,List
from rest.schemas.chart_request import *
import uuid,shutil,sys,os
from dependencies import *
from application.exceptions import *
from ..exceptions import *


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

        return FileResponse(tmpath, media_type="image/png")

    except ChartParsingError as e:
        raise HTTPException(status_code=400,detail=e)

    except IncorrectChartType as e:
        raise HTTPException(status_code=400,detail=e)

    except ChartStrategyNotFound as e:
        raise HTTPException(status_code=400,detail=e)

    except Exception as e:
        raise HTTPException(status_code=500,detail=e)

    finally:

        tasks.add_task(temp.remove_temp_file,tmpath)

@router.post("/generate-save-chart-file")
def generate_chart_file(
    req: SaveChartRequest,
    chart_strategy_factory = Depends(get_chart_strategy_factory),
    mapper = Depends(get_rest_chart_mapper), 
    imgs = Depends(get_images_repo),
    ):

    chart = req.chart
    filename  = req.filename
    path =  imgs.prepare_path(filename)

    try:
        model = mapper.map_to_model(chart)
        chart_strategy_factory.generate_to_file(model,path)

        return FileResponse(path, media_type="image/png")

    except ChartParsingError as e:
        raise HTTPException(status_code=400,detail=e)

    except IncorrectChartType as e:
        raise HTTPException(status_code=400,detail=e)

    except ChartStrategyNotFound as e:
        raise HTTPException(status_code=400,detail=e)

    except Exception as e:
        raise HTTPException(status_code=500,detail=e)


