from fastapi import APIRouter, Query, Depends, Response
from fastapi import status
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Dict, Any, Optional,List
import uuid,shutil,sys,os
from dependencies import *

router = APIRouter()

@router.post("/upload/", status_code=201)                                                          
async def upload_template(file: UploadFile = File(...),templates=Depends(get_templates_service)):
    """                                                                                                   
    Uploads a new Jinja2 HTML template file.                                                              
                                                                                                        
    Args:                                                                                                 
        file (UploadFile): The template file to upload. Must have a .j2 extension.                        
                                                                                                        
    Returns:                                                                                              
        Dict[str, str]: A message indicating success and the filename.                                    
                                                                                                        
    Raises:                                                                                               
        HTTPException:                                                                                    
            - 400 Bad Request: If the file extension is not .j2 or if the file already exists.            
            - 500 Internal Server Error: For any file writing errors.                                     
    """                                                                                                   
    try:                                                                                                  
        templates.save_template(file.filename,file.file)
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not save template file: {e}")                 
                                                                                                        
    return {"message": f"Template '{file.filename}' uploaded successfully."}                              
                                                                                                        
@router.get("/", response_model=List[str])                                                         
async def list_templates(templates=Depends(get_templates_service)) -> List[str]:                                                                  
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  
        return templates.get_all_templates()
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  

@router.get("/byname", response_model=str)                                                         
async def get_template(template_name:str,templates=Depends(get_templates_service)) -> str:
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  
        return templates.get_template(template_name)
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  

@router.delete("/")
async def remove_template(template_name:str,templates=Depends(get_templates_service)) -> str:
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  
        templates.remove_template(template_name)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  