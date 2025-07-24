from domain.value_objects.pdfs import *
from ..exceptions import *
import os,sys,shutil
import jinja2
from weasyprint import HTML, CSS


class PDFService():
    def __init__(self, log,temp_service,templates_dir,themes_dir,static_dir):
        self.temp_service=temp_service
        self.log = log
        self.themes_dir=themes_dir
        self.templates_dir=templates_dir
        self.static_dir=static_dir

    def generate_to_file(self,data:PDFData,output_path:str):

        template_data = data.params

        template_loader = jinja2.FileSystemLoader(searchpath=self.templates_dir)
        template_env = jinja2.Environment(loader=template_loader, undefined=jinja2.StrictUndefined)

        try:
            template = template_env.get_template(data.template_name+".html.j2")
            rendered_html = template.render(template_data)
        except jinja2.TemplateNotFound:
            raise TemplateNotFoundError(f"Template '{data.template_name}' not found.")
        except jinja2.UndefinedError as e:
            #raise InvalidDataError(f"The template requires data that was not provided: {e.message}")
            pass

        theme_path = os.path.join(self.themes_dir, data.theme_name)
        if(not str(theme_path)[-4:]==".css"):
            theme_path+=".css"
        if not os.path.exists(theme_path):
            theme_path = os.path.join(self.themes_dir, 'style.css')

        html = HTML(string=rendered_html, base_url=self.static_dir)
        css = CSS(filename=theme_path)
        html.write_pdf(output_path, stylesheets=[css])
