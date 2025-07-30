import os,sys,shutil
from ..exceptions import *

class ImagesRepo():
    def __init__(self,log,imagesdir):
        self.log = log
        self.imagesdir=imagesdir
        os.makedirs(self.imagesdir,exist_ok=True)

    def save(self,filename:str,fileobject):
        """"
        Filename should have correct extension for given file object
        """

        file_path = os.path.join(self.imagesdir,filename)
        try:
            with open(file_path, "wb") as buffer:                                                             
                shutil.copyfileobj(fileobject, buffer)                                                         

        except Exception as e:
            raise ImageSaveError()

    def get_dir(self):
        return self.imagesdir

    def get_file_extension(self,file):
        return file.split(".")[1]

    
    def get_full_path(self,imgname:str)->str:

        filepath = os.path.join(self.imagesdir,imgname)

        if not os.path.exists(filepath):
            raise ImageNotFoundError()
        
        return filepath

    def list_all(self)->list[str]:
        """"
        Returns list of all images
        """
        try:
            templates = os.listdir(self.imagesdir)
            return [f for f in templates if os.path.isfile(os.path.join(self.imagesdir, f))]
        except FileNotFoundError:
            return []
        except Exception as e:
            return []

    def remove(self,filename):
        imgpath = self.get_full_path(filename)
        try:
            if not os.path.exists(imgpath):
                self.log.debug("Image not found")
                raise ImageNotFoundError()

            os.remove(imgpath)
            return True

        except FileNotFoundError:
            raise ImageNotFoundError()




