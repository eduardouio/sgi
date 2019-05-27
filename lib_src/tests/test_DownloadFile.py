#!/usr/bin/python3
import io
import urllib

from PyPDF2 import PdfFileReader
import requests
from django.test import TestCase
from lib_src import DownloadFile
from lib_src.DownloadFile import PyPDF2


class TestDownloadFile(TestCase):
    
    def setUp(self):    
        self.url_dai = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptBpIclDclDtlInqrPrn-date-20190415-1F00BBB3-220E-8BAF-F8D5-7459FAE0E4EA.pdf'
        self.url_tributos = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptRcTrBillInqrPrn-date-20190415-1EE54180-BD19-5481-123F-8B72B1676BD4.pdf'
        self.url_ajustes = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptRcTrBillInqrPrn-date-20190415-1EE54180-BD19-5481-123F-8B72B1676BD4.pdf'
        self.url_etiquetas = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptRcTrBillInqrPrn-date-20190415-1EEA442F-700F-CDC7-2B5E-63655274E41A.pdf'
        self.download_file = DownloadFile()
        return super().setUp()

    def test_get_file(self):
        #fail url
        with self.assertRaises(Exception) as e:
            self.download_file.get_file('http://ecuapass.aduana.gob.ec/ipt_server/')
        self.assertEqual(e.exception.__str__(), 'Url no encontrada')
        
        #url-not-pdf
        with self.assertRaises(Exception) as ex:
            self.download_file.get_file('http://ecuapass.aduana.gob.ec/')
        self.assertEqual(ex.exception.__str__(), 'Archivo no compatible')

        #succes url
        pdf_file_dai = self.download_file.get_file(self.url_dai)
        self.assertIsInstance(pdf_file_dai, PdfFileReader)
    
    def test_get_dai_data(self):
        data = {
            'document_number': '055-2019-10-00271175',
            'category': 'DAI',
            'ruc_empresa': '1790023516001',
            'empresa': 'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.',
            'fecha_aceptacion': '15/04/2019',
            'declarante': 'PONCE NOLIVOS MARIO FABIAN',
            'ruc_declarante': '1703505030001',
        }
        self.assertDictEqual(self.download_file.get_data('dai', self.url_dai), data)


    def test_with_other_document(self):
        with self.assertRaises(Exception) as e:
            self.download_file.get_data('dai', self.url_tributos)
        self.assertEqual(e.exception.__str__(),
                         'El documento no correponde a lo indicado')

        with self.assertRaises(Exception) as e:
            self.download_file.get_data('tributos', self.url_etiquetas)
        self.assertEqual(e.exception.__str__(),
                         'El documento no correponde a lo indicado')
        
        with self.assertRaises(Exception) as e:
            self.download_file.get_data('etiquetas', self.url_tributos)
        self.assertEqual(e.exception.__str__(),
                         'El documento no correponde a lo indicado')

    def test_get_tributes_data(self):
        data = {
            'document_number': '40174824',
            'category': 'TRIBUTOS',
            'ruc_empresa': '1790023516001',
            'fecha_liquidacion' : '15/04/2019',
            'empresa': 'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.',
            #'arancel_advalorem' : 0,
            #'arancel_especifico' : 0,
            #'fondinfa': 18.84,
            #'ice_especifico': 1242.360,
            #'ice_advalorem': 0,
        }
        self.assertDictEqual(self.download_file.get_data('tributos', self.url_tributos ), data)

    def test_get_triutes_full(self):
        data = {
           'document_number': '40221493',
            'category': 'TRIBUTOS',
            'ruc_empresa': '1792324289001',
            'fecha_liquidacion': '09/05/2019',
            'empresa': 'IMNAC IMPORTADORA NACIONAL CIA. LTDA.',
            #'arancel_advalorem': 29.92,
            #'arancel_especifico': 0,
            #'fondinfa': 16.26,
            #'ice_especifico': 495.90,
            #'ice_advalorem': 3069.36,
        }
        self.assertDictEqual(self.download_file.get_data(
            'tributos', 'http://localhost:9999/40221493.pdf'), data)

    def test_get_pdf_file(self):
        self.assertTrue(self.download_file.get_pdf_file(self.url_tributos))