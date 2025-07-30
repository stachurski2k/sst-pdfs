from fastapi import APIRouter, Query, Depends, Response
from fastapi import status
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Dict, Any, Optional,List
import uuid,shutil,sys,os
from dependencies import *
import magic

router = APIRouter()

@router.post("/upload/", status_code=201)                                                          
async def upload_image(file: UploadFile = File(...),imgs=Depends(get_images_repo)):
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
        imgs.save(file.filename,file.file)
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not save template file: {e}")                 
                                                                                                        
    return {"message": f"Template '{file.filename}' uploaded successfully."}                              
                                                                                                        
@router.get("/", response_model=List[str])                                                         
async def list_images(imgs=Depends(get_images_repo)) -> List[str]:                                                                  
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  
        return imgs.list_all()
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  

@router.get("/byname", response_model=str)                                                         
async def get_image(imgname:str,imgs=Depends(get_images_repo)) -> str:
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  

        image_path = imgs.get_full_path(imgname)
        mime_type = magic.from_file(image_path, mime=True)
        return FileResponse(image_path, media_type=mime_type)

    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  

@router.delete("/")
async def remove_image(imgname:str,imgs=Depends(get_images_repo)) -> str:
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  
        imgs.remove(imgname)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  