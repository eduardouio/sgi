#!/usr/bin/python3
import requests
import PyPDF2
import io
import urllib
url = 'http://ecuapass.aduana.gob.ec/ipt_server/cmmReportPdfController.do?method=runPdfReport&fileName=/attach/report/jsp/jasper/report/portal/IptBpIclDclDtlInqrPrn-date-20190403-856E9440-CA19-0EF7-488B-D3BD35841D48.pdf'

pdfFile = io.BytesIO(requests.get(url).content)
#pdfFile = urllib.request.urlopen(url).read()
writer = PyPDF2.PdfFileWriter()
#memoryFile = StringIO(pdfFile)

#with open("tutorial1.pdf", "wb") as code:
#    code.write(pdfFile)

pdfReader = PyPDF2.PdfFileReader(pdfFile)
for p in range(0,pdfReader.numPages):
    page = pdfReader.getPage(p)
    print(page.extractText())

#for pageNum in xrange(pdfFile.getNumPages()):
#        currentPage = pdfFile.getPage(pageNum)
#        writer.addPage(currentPage)
#
#
#outputStream = open("output.pdf", "wb")
#writer.write(outputStream)
#outputStream.close()
