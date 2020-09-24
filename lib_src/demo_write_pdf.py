#!/usr/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
can.setFillColorRGB(0,0.4,0.8)
can.setFontSize(18)
can.drawString(60, 800, "055-2019-10-00256541")
can.setFontSize(12)
can.drawString(510, 600, "015/19")
can.setFontSize(10)
can.drawString(497, 580, "GONZALEZ")
can.drawString(497, 560, "UIO PARCIAL 1")
can.drawString(497, 540, "GRADO ALCOH")
can.drawString(497, 520, "F: 25/05/2019")
can.drawString(497, 500, "H: 13:10:10")
can.drawString(497, 480, "EVILLOTA")
can.setFontSize(12)
can.drawString(385, 90, "PONCE NOLIVOS MARIO FABIAN")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("40173334.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()