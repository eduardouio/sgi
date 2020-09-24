#!/usr/bin/python3
import io
import re
import urllib

import PyPDF2
import requests

from logs.app_log import loggin


class DownloadFile(object):

    def __init__(self):
        """
        Clase encaragda de obtener un archivo desde internet 
            DAI
            Liquidacion Etiquetas
            Liquidacion de Tributos
        
        """
        self.url = None
        self.type_document = None
        self.pdfReader = None
        self.data = {
            'document_number':None,
            'category': None,
            'fecha_aceptacion': None,
            'empresa': None,
            'ciudad': None,
            'agente': None,
            'ruc_agente': None,

        }

    def get_file(self,  url):
        loggin('i', 'Iniciando desdarga desde portal SENAE') 
        response = requests.get(url)
        if response.status_code != 200:
            loggin('e', 'Archivo de en url {} no existe'.format(url))
            raise Exception('Url no encontrada')
        
        if response.headers['content-type'] != 'application/pdf':
            raise Exception('Archivo no compatible')

        loggin('e', response.headers['content-type'])
        pdf_file = io.BytesIO(response.content)
        self.pdfReader = PyPDF2.PdfFileReader(pdf_file)
        return self.pdfReader
    
    def get_data(self, category, url):
        pdf_reader = self.get_file(url)
        if self.check_category(category, pdf_reader) == False:
            raise Exception('El documento no correponde a lo indicado')

        if category == 'dai':
            return self.get_dai_data(pdf_reader)
        
        if category == 'tributos':
            return self.get_tributes_data(pdf_reader)
    
    def get_dai_data(self, pdf_reader):
        text_page = pdf_reader.getPage(0).extractText()
        dai = re.findall(
            '[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', text_page
            )
        rucs = re.findall(
            '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', text_page)
        fecha_aceptacion = re.findall(
            '[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]',text_page)

        return {
            'document_number': dai[0],
            'category': 'DAI',
            'ruc_empresa': rucs[0],
            'empresa': empresas[rucs[0]],
            'fecha_aceptacion': fecha_aceptacion[0],
            'declarante': agentes[rucs[1]],
            'ruc_declarante': rucs[1],
        }

    def get_tributes_data(self, pdf_reader):
        text_page = pdf_reader.getPage(0).extractText()
        loggin('t', text_page)
        fechas = re.findall('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]', text_page)
        lista = text_page.replace(',', '').replace(
            ':', ' ').replace('arancelarios', 'arancelarios ').split(' ')
        lista = [item for item in lista if(item)]
        loggin('t', lista)
        numbers = rr = re.findall(
            "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", text_page)
        return {
            'document_number': numbers[3],
            'category': 'TRIBUTOS',
            'ruc_empresa': numbers[4][:13],
            'fecha_liquidacion': fechas[2],
            'empresa': empresas[numbers[4][:13]],
            #'arancel_advalorem': float(lista[22]),
            #'arancel_especifico': 0,
            #'fondinfa': 0,
            #'ice_especifico': 0,
            #'ice_advalorem': 0,
        }
    
    def get_pdf_file(self, url):
        pdf_reader = self.get_file(url)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(0, pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page))
        loggin('t', pdf_writer)
        return True

    def check_category(self,category,pdf_reader):
        text_page = pdf_reader.getPage(0).extractText()
        dai = bool(re.findall(
            '[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', text_page
        ))
        etiquetas = bool(re.findall('ETIQUETAS FISCALES', text_page))
        
        if category == 'dai' and dai:
            return True
        
        if category == 'etiquetas' and etiquetas:
            return True
        
        if category == 'tributos' and not dai and not etiquetas:
            return True
        
        return False

