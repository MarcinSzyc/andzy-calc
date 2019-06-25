from .models import Renovation, PRODUCT_TYPE
from functools import reduce


def renovation_summary(worksheet, workbook, pk):
    renovation = Renovation.objects.get(pk=pk)
    bold = workbook.add_format({'bold': True, 'center_across': True})
    background = workbook.add_format()
    background.set_bg_color('white')
    summary_formatting = workbook.add_format(
        {'bold': True, 'font_size': 32, 'center_across': True, 'bg_color': 'green'})
    description_title_formatting = workbook.add_format({'font_size': 22, 'center_across': True})
    description_formatting = workbook.add_format({'center_across': True})
    date_format = workbook.add_format({'num_format': 'd mmmm yyyy', 'center_across': True})
    worksheet.merge_range('A1:D1', renovation.name, summary_formatting)
    worksheet.merge_range('A2:D2', 'Description', description_title_formatting)
    worksheet.merge_range('A3:D3', renovation.description, description_formatting)
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


def room_measurements(room_worksheet, workbook, room):
    bold = workbook.add_format({'bold': True, 'center_across': True})
    measurements_formatting = workbook.add_format(
        {'bold': True, 'font_size': 22, 'center_across': True, 'bg_color': 'yellow'})
    room_worksheet.merge_range('F1:I1', 'Measurements', measurements_formatting)
    room_worksheet.write('F2', 'Width', bold)
    room_worksheet.write('G2', 'Length', bold)
    room_worksheet.write('H2', 'Height', bold)
    room_worksheet.write('I2', 'Tiles Height', bold)
    room_worksheet.write('F3', room.width)
    room_worksheet.write('G3', room.length)
    room_worksheet.write('H3', room.height)
    room_worksheet.write('I3', room.tiles_height)


def room_surface_floor(room):
    return room.width * room.length


def room_surface_walls(room):
    length_wall = room.length * room.height
    width_wall = room.width * room.height
    return 2 * (length_wall + width_wall)


def room_surface_ceiling(room):
    return room.width * room.length


def room_surface_tiles(room):
    length_tiles_wall = room.length * room.tiles_height
    width_tiles_wall = room.width * room.tiles_height
    return 2 * (length_tiles_wall + width_tiles_wall)


def room_surfaces(room_worksheet, workbook, room):
    bold = workbook.add_format({'bold': True, 'center_across': True})
    surfaces_formatting = workbook.add_format(
        {'bold': True, 'font_size': 22, 'center_across': True, 'bg_color': 'yellow'})
    room_worksheet.merge_range('F5:I5', 'Surfaces', surfaces_formatting)
    room_worksheet.write('F6', 'Floor', bold)
    room_worksheet.write('G6', 'Walls', bold)
    room_worksheet.write('H6', 'Ceiling', bold)
    room_worksheet.write('I6', 'Tiles', bold)
    room_worksheet.write('F7', room_surface_floor(room))
    room_worksheet.write('G7', room_surface_walls(room))
    room_worksheet.write('H7', room_surface_ceiling(room))
    room_worksheet.write('I7', room_surface_tiles(room))


def room_cost(room_worksheet, workbook, room):
    bold = workbook.add_format({'bold': True, 'center_across': True})
    cost_formatting = workbook.add_format(
        {'bold': True, 'font_size': 22, 'center_across': True, 'bg_color': 'yellow'})
    room_worksheet.merge_range('F10:I10', 'Cost', cost_formatting)
    room_worksheet.write('F11', 'Floor', bold)
    room_worksheet.write('G11', 'Walls', bold)
    room_worksheet.write('H11', 'Ceiling', bold)
    room_worksheet.write('I11', 'Tiles', bold)
    room_worksheet.write('F13', 'Sum', bold)
    room_worksheet.write('F14', 'Labor', bold)
    room_worksheet.write('F15', 'Total', bold)
    room_worksheet.write('F12', room.cost.floor)
    room_worksheet.write('G12', room.cost.walls)
    room_worksheet.write('H12', room.cost.ceiling)
    room_worksheet.write('I12', room.cost.tiles)
    room_worksheet.write('G13', room.cost.basic_sum)
    room_worksheet.write('G14', room.cost.labor)
    room_worksheet.write('G15', room.cost.total_sum)


def room_product(room_worksheet, workbook, product, row):
    bold = workbook.add_format({'bold': True, 'center_across': True})
    room_worksheet.write('A9', 'Product', bold)
    room_worksheet.write('B9', 'Type', bold)
    room_worksheet.write('C9', 'Price', bold)
    room_worksheet.write(f'A{row}', product.name)
    for item in PRODUCT_TYPE:
        if item[0] == product.type:
            product_type = item[1]
    room_worksheet.write(f'B{row}', product_type)
    room_worksheet.write(f'C{row}', product.price)


def room_view_cell_sizeing(room_worksheet, workbook):
    background = workbook.add_format()
    background.set_bg_color('white')
    room_worksheet.set_row(0, 36)
    room_worksheet.set_row(4, 32)
    room_worksheet.set_row(9, 36)
    room_worksheet.set_column(0, 40, cell_format=background)


def renovation_room_summary(workbook, pk):
    renovation = Renovation.objects.get(pk=pk)
    summary_formatting = workbook.add_format(
        {'bold': True, 'font_size': 32, 'center_across': True, 'bg_color': 'yellow'})
    description_formatting = workbook.add_format({'font_size': 22, 'center_across': True})
    bold = workbook.add_format({'bold': True, 'center_across': True})
    for room in renovation.room_set.all():
        room_worksheet = workbook.add_worksheet(room.name)
        room_worksheet.merge_range('A1:D1', room.name, summary_formatting)
        room_worksheet.merge_range('A2:D2', room.description, description_formatting)
        room_worksheet.write('A2', 'Id', bold)
        room_worksheet.write('B2', 'Type', bold)
        room_worksheet.write('C2', 'Renovation', bold)
        room_worksheet.write('C2', 'Total Cost', bold)
        room_worksheet.write('A3', room.id)
        room_worksheet.write('B3', room.type)
        room_worksheet.write('C3', room.renovation.name)
        room_worksheet.write('D3', room.cost.total_sum)
        row = 10
        for product in room.product.all():
            room_product(room_worksheet, workbook, product, row)
            row += 1
        room_measurements(room_worksheet, workbook, room)
        room_surfaces(room_worksheet, workbook, room)
        room_cost(room_worksheet, workbook, room)
        room_view_cell_sizeing(room_worksheet, workbook)
