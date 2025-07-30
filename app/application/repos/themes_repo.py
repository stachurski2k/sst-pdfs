import os,shutil,sys
from ..exceptions import *

class ThemesRepo():

    def __init__(self,log,themespath):
        self.log = log
        self.themesdir=themespath
        os.makedirs(self.themesdir, exist_ok=True)

    def save(self,filename:str,file):
        """
        file is FileObject
        """
        file_path = os.path.join(self.themesdir,filename)
        try:
            with open(file_path, "wb") as buffer:                                                             
                shutil.copyfileobj(file, buffer)                                                         

        except Exception as e:
            raise ThemeUploadError()

    def get_full_path(self,themename:str)->str:

        filepath = os.path.join(self.themesdir,themename)

        if not os.path.exists(filepath):
            filepath +=".css"
            if not os.path.exists(filepath):
                raise ThemeNotFoundError()
        
        return filepath

    def get_dir(self):
        return self.themesdir

    def list_all(self) -> list[str]:
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

    def get_content(self,theme_name: str)->str:
        """
        Retrieves the content of a specific theme file.
        Args:
            theme_name (str): The name of the theme file.
        Returns:
            str: Content of a file
        Raises:
            ThemeNotFoundException: If theme does not exist
        """
        theme_path = self.get_full_path(themename=theme_name)

        try:
            with open(theme_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            raise ThemeNotFoundError()

    def remove(self,theme_name: str)->bool:
        """
        Removes a specific theme file.

        Args:
            theme_name (str): The name of the theme file to remove.

        Returns:
            bool: True if the theme was successfully removed, False otherwise.
        """
        theme_path = self.get_full_path(themename=theme_name)
        try:
            if not os.path.exists(theme_path):
                raise ThemeNotFoundError()

            os.remove(theme_path)
            return True

        except FileNotFoundError:
            raise ThemeNotFoundError()