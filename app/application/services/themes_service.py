import os,shutil,sys
from ..exceptions import *

class ThemesService():
    def __init__(self,log,themespath):
        self.log = log
        self.themesdir=themespath
        os.makedirs(self.themesdir, exist_ok=True)

    def save_theme(self,filename:str,file):
        """
        file is FileObject
        """
        file_path = os.path.join(self.themesdir,filename)
        try:
            with open(file_path, "wb") as buffer:                                                             
                shutil.copyfileobj(file, buffer)                                                         

        except Exception as e:
            raise ThemeUploadException()


    def get_all_themes(self) -> list[str]:
        """
        Retrieves a list of all theme filenames in the CUSTOM_THEMES_DIR.

        Returns:
            List[str]: A list of theme filenames.
        """
        try:
            theme_files = os.listdir(self.themesdir)
            return [f for f in theme_files if os.path.isfile(os.path.join(self.themesdir, f))]
        except FileNotFoundError:
            return []
        except Exception as e:
            return []

    def get_theme(self,theme_name: str)->str:
        """
        Retrieves the content of a specific theme file.
        Args:
            theme_name (str): The name of the theme file.
        Returns:
            str: Content of a file
        Raises:
            ThemeNotFoundException: If theme does not exist
        """
        theme_path = os.path.join(self.themesdir, theme_name)
        if not os.path.exists(theme_path):
           theme_path= theme_path+".css" 

        try:
            with open(theme_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            raise ThemeNotFoundException()

    def remove_theme(self,theme_name: str)->bool:
        """
        Removes a specific theme file.

        Args:
            theme_name (str): The name of the theme file to remove.

        Returns:
            bool: True if the theme was successfully removed, False otherwise.
        """
        theme_path = os.path.join(self.themesdir, theme_name)
        try:
            if not os.path.exists(theme_path):
                raise ThemeNotFoundException

            os.remove(theme_path)
            return True

        except FileNotFoundError:
            raise ThemeNotFoundException