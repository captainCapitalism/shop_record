import openpyxl as oxl

wb = oxl.Workbook()

dest_filename = 'help.xlsx'
ws1 = wb.active
ws1.title = "testzz"
ws1['B2'] = "hellp"
wb.save(filename=dest_filename)

wb.save(dest_filename)
