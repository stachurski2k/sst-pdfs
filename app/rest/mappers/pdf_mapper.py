import os
from rest.schemas.chart_request import *
from rest.schemas.pdf_request import *
from domain.value_objects.charts import *
from domain.value_objects.pdfs import *
from rest.exceptions import *

class PDFMapper():
    def __init__(self,log,imgs):
        self.log=log
        self.imgs= imgs

    def map_to_pdfdata(self,req: PDFRequest):

        for img_key,img_mock in req.images.items():
            req.params[img_key] = "file://"+os.path.abspath(self.imgs.get_full_path(img_mock) )
            self.log.debug(req.params[img_key])

        return PDFData(
            template_name=req.template_name,
            theme_name=req.theme_name,
            params=req.params
        )