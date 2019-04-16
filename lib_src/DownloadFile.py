#!/usr/bin/python3
import io
import urllib

import PyPDF2
import requests
import re


class DownloadFile(object):
    
    def __init__(self, url, type_document):
        ''' 
        obtiene unn fichero desde el portal de la senae y obtiene informacion
        relevante del texto
    
        Arguments:
            type_document {string}
                tipo de documentop a descargar [DAI | LIQUIDACION]
        '''
        self.url = url
        self.type_document = type_document
        self.pdf = None
        self.text_pages = []
        self.pdf = io.BytesIO(requests.get(url).content)
        self.data = None
        pdfReader = PyPDF2.PdfFileReader(self.pdf)
        #writer = PyPDF2.PdfFileWriter()
        for p in range(0, pdfReader.numPages):
            page = pdfReader.getPage(p)
            self.text_pages.append(page.extractText())
        
    def get_text_from_file(self):
        self.data = {
            'nro_dai' : None,
            'fecha_aceptacion' : None,
            'empresa' : None,
            'ciudad' : None,
            'agente' : None,
            'ruc_agente' : None,
        }
        for page in self.text_pages:
            print(page)
        
    
    def write_pdf(self):
        pass
    
    def get_file(self):
        pass


url = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptBpIclDclDtlInqrPrn-date-20190403-856E9440-CA19-0EF7-488B-D3BD35841D48.pdf'
#url = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptRcTrBillInqrPrn-date-20190403-8566C71D-B30A-570D-C807-49F301973987.pdf'

dw = DownloadFile(url, 'DAI')
dw.get_text_from_file()
