from .models import Renovation, Room
from functools import reduce


def renovation_summary(worksheet, workbook, pk):
    renovation = Renovation.objects.get(pk=pk)
    bold = workbook.add_format({'bold': True, 'center_across': True})
    background = workbook.add_format()
    background.set_bg_color('white')
    summary_formating = workbook.add_format({'bold': True, 'font_size': 32, 'center_across': True, 'bg_color': 'green'})
    description_title_formating = workbook.add_format({'font_size': 22, 'center_across': True})
    description_formating = workbook.add_format({'center_across': True})
    date_format = workbook.add_format({'num_format': 'd mmmm yyyy', 'center_across': True})
    worksheet.merge_range('A1:D1', renovation.name, summary_formating)
    worksheet.merge_range('A2:D2', 'Description', description_title_formating)
    worksheet.merge_range('A3:D3', renovation.description, description_formating)
    worksheet.write('A4', 'Id', bold)
    worksheet.write('B4', 'Date', bold)
    worksheet.write('C4', 'Rooms', bold)
    worksheet.write('D4', 'Total Cost', bold)
    worksheet.write("A5", renovation.id)
    renovation_date = Renovation.objects.get(pk=pk).date
    worksheet.write("B5", renovation_date.replace(tzinfo=None), date_format)
    worksheet.write("C5", renovation.room_set.all().count())
    total_cost = round(
        reduce((lambda x, y: x + y), [room.cost.total_sum for room in Renovation.objects.get(
            pk=pk).room_set.all()]), 2)
    worksheet.write("D5", total_cost)
    worksheet.set_column(0, 40, cell_format=background)
    worksheet.set_row(0, 36)
    worksheet.set_row(1, 27)


def renovation_room_cost(worksheet, workbook, pk):
    bold = workbook.add_format({'bold': True})
    worksheet.write('A7', 'Room', bold)
    worksheet.write('B7', 'Cost', bold)
    row = 7
    for room in Renovation.objects.get(pk=pk).room_set.all():
        worksheet.write(
            row,
            0,
            room.name
        )
        row += 1
    row = 7
    for room in Renovation.objects.get(pk=pk).room_set.all():
        worksheet.write(
            row,
            1,
            room.cost.total_sum
        )
        row += 1


def renovation_room_summary(worksheet, workbook, room):
    pass
