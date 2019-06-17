from .models import Renovation
import xlsxwriter


def renovation_summary(worksheet, workbook, pk):
    renovation = Renovation.objects.get(pk=pk)
    bold = workbook.add_format({'bold': True})
    background = workbook.add_format()
    background.set_bg_color('white')
    summary_font = workbook.add_format({'bold': True, 'font_size': 32})
    date_format = workbook.add_format({'num_format': 'd mmmm yyyy'})
    worksheet.write('A1', 'Summary', summary_font)
    worksheet.write('A2', 'Id', bold)
    worksheet.write('B2', 'Name', bold)
    worksheet.write('C2', 'Description', bold)
    worksheet.write('D2', 'Date', bold)
    worksheet.write('E2', 'Rooms', bold)
    worksheet.write("A3", renovation.id)
    worksheet.write("B3", renovation.name)
    worksheet.write("C3", renovation.description)
    renovation_date = Renovation.objects.get(pk=pk).date
    worksheet.write("D3", renovation_date.replace(tzinfo=None), date_format)
    worksheet.write("E3", renovation.room_set.all().count())
    worksheet.set_column(0, 40, cell_format=background)
