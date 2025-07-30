from domain.value_objects.pdfs import *
from ..exceptions import *
import os,sys,shutil
import jinja2
from weasyprint import HTML, CSS


class PDFService():
    def __init__(self, log,workdir,templates_repo,themes_repo):

        self.log = log
        self.templates_repo=templates_repo
        self.themes_repo = themes_repo
        self.workdir=workdir

    def generate_to_file(self,data:PDFData,output_path:str):

        template_data = data.params

        template_loader = jinja2.FileSystemLoader(searchpath=self.workdir)
        template_env = jinja2.Environment(loader=template_loader, undefined=jinja2.StrictUndefined)

        try:
            template = template_env.get_template(self.templates_repo.get_full_path(data.template_name))
            rendered_html = template.render(template_data)

        except jinja2.TemplateNotFound:
            raise TemplateNotFoundError(f"Template '{data.template_name}' not found.")

        except jinja2.UndefinedError as e:
            raise PDFGenerationError(f"The template requires data that was not provided: {e.message}")

        theme_path = self.themes_repo.get_full_path(data.theme_name)

        if not os.path.exists(theme_path):
            raise ThemeNotFoundError()

        html = HTML(string=rendered_html, base_url=self.workdir)
        css = CSS(filename=theme_path)
        html.write_pdf(output_path, stylesheets=[css])
