import openpyxl as op

wb = op.load_workbook('format.xlsx')
ws = wb.get_sheet_by_name('Hoja1')
ws['A4'] = 'Esto es Esparta!'
wb.save('sample.xlsx')
wb.close()