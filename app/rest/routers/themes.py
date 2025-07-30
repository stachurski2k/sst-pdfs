from fastapi import APIRouter, Query, Depends
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form,Response,status
from typing import Dict, Any, Optional,List
import uuid,shutil,sys,os
from fastapi import status
from application.exceptions import *
from dependencies import *

router = APIRouter()

@router.post("/upload/", status_code=201)                                                             
async def upload_theme(file: UploadFile = File(...),themes=Depends(get_themes_repo)) -> Dict[str, str]:                                   
    """                                                                                                   
    Uploads a new CSS theme file.                                                                         
                                                                                                        
    Args:                                                                                                 
        file (UploadFile): The theme file to upload. Must have a .css extension.                          
                                                                                                        
    Returns:                                                                                              
        Dict[str, str]: A message indicating success and the filename.                                    
                                                                                                        
    Raises:                                                                                               
        HTTPException:                                                                                    
            - 400 Bad Request: If the file extension is not .css or if the file already exists.           
            - 500 Internal Server Error: For any file writing errors.                                     
    """                                                                                                   
    
    try:
        themes.save(file.filename,file.file)
        return Response(status_code=status.HTTP_200_OK) 
    except Exception as e:
        raise HTTPException(status_code= 500,detail = e)
    
@router.get("/", response_model=List[str])
async def list_themes(themes=Depends(get_themes_repo))->List[str]:                                                         

    """                                                                                                   
    Lists all available CSS theme files.                                                                  
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of theme filenames.                                                             
    """                                                                                                   
    
    return themes.list_all()

@router.get("/byname", response_model=str)                                                            
async def list_themes(filename : str, themes= Depends(get_themes_repo) ) -> str:                                                                     
    """                                                                                                   
    Lists all available CSS theme files.                                                                  
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of theme filenames.                                                             
    """                                                                                                   
    try:
        return themes.get_content(filename)

    except ThemeNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"Theme {filename} not found!")

@router.delete("/", response_model=str)                                                            
async def remove_theme(filename : str, themes= Depends(get_themes_repo) ) -> str:                                                                     
    """                                                                                                   
    Lists all available CSS theme files.                                                                  
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of theme filenames.                                                             
    """                                                                                                   
    try:
        themes.remove(filename)
        return Response(status_code=status.HTTP_200_OK)

    except ThemeNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"Theme {filename} not found!")
    