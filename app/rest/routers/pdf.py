from fastapi import APIRouter, Query, Depends
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form,Response,status
from typing import Dict, Any, Optional,List
import uuid,shutil,sys,os
from fastapi import status
from application.services.themes_service import *
from dependencies import *

router = APIRouter()

@router.post("/generate-pdf-file")
def generate_pdf_file():