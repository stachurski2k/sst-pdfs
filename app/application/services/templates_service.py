import os,shutil,sys
from ..exceptions import *

class TemplatesService():
    def __init__(self,log,templatesdir):
        self.log = log
        self.templatesdir=templatesdir
        os.makedirs(self.templatesdir, exist_ok=True)

    def save_template(self,filename:str,file):
        """
        file is FileObject
        """
        file_path = os.path.join(self.templatesdir,filename)
        try:
            with open(file_path, "wb") as buffer:                                                             
                shutil.copyfileobj(file, buffer)                                                         

        except Exception as e:
            raise TemplateSaveError()


    def get_all_templates(self) -> list[str]:
        """
        Retrieves a list of all theme filenames in the CUSTOM_THEMES_DIR.

        Returns:
            List[str]: A list of theme filenames.
        """
        try:
            templates = os.listdir(self.templatesdir)
            return [f for f in templates if os.path.isfile(os.path.join(self.templatesdir, f))]
        except FileNotFoundError:
            return []
        except Exception as e:
            return []

    def get_template(self,template_name: str)->str:
        """
        Retrieves the content of a specific theme file.
        Args:
            theme_name (str): The name of the theme file.
        Returns:
            str: Content of a file
        Raises:
            ThemeNotFoundException: If theme does not exist
        """
        templattepath = os.path.join(self.templatesdir, template_name)
        if not os.path.exists(templattepath):
           templattepath= templattepath+".html.j2" 

        try:
            with open(templattepath, "r") as f:
                return f.read()
        except FileNotFoundError:
            raise TemplateNotFoundError()

    def remove_template(self,template_name: str)->bool:
        """
        Removes a specific theme file.

        Args:
            theme_name (str): The name of the theme file to remove.

        Returns:
            bool: True if the theme was successfully removed, False otherwise.
        """
        templatepath = os.path.join(self.templatesdir, template_name)
        try:
            if not os.path.exists(templatepath):
                self.log.debug("Template not found")
                raise TemplateNotFoundError()

            os.remove(templatepath)
            return True

        except FileNotFoundError:
            raise TemplateNotFoundError()