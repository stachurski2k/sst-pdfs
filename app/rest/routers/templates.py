from fastapi import APIRouter, Query
from fastapi import FastAPI, Body, Query, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Dict, Any, Optional,List
import uuid,shutil,sys,os

router = APIRouter()

@router.post("/upload/", status_code=201)                                                          
async def upload_template(file: UploadFile = File(...)) -> Dict[str, str]:                                
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
    if not file.filename.endswith(".j2"):                                                                 
        raise HTTPException(status_code=400, detail="Invalid file type. Only .j2 files are allowed")
                                                                                                        
    file_path = os.path.join(TEMPLATES_DIR, file.filename)                                                
    try:                                                                                                  
        with open(file_path, "wb") as buffer:                                                             
            shutil.copyfileobj(file.file, buffer)                                                         
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not save template file: {e}")                 
                                                                                                        
    return {"message": f"Template '{file.filename}' uploaded successfully."}                              
                                                                                                        
@router.get("/", response_model=List[str])                                                         
async def list_templates() -> List[str]:                                                                  
    """                                                                                                   
    Lists all available Jinja2 HTML template files.                                                       
                                                                                                        
    Returns:                                                                                              
        List[str]: A list of template filenames.                                                          
    """                                                                                                   
    try:                                                                                                  
        templates = [f for f in os.listdir(TEMPLATES_DIR) if f.endswith(".j2")]                           
        return templates                                                                                  
    except Exception as e:                                                                                
        raise HTTPException(status_code=500, detail=f"Could not list templates: {e}")  