import xlwt
from fontTools.ttLib import TTFont

font = TTFont("kaitigb2312.ttf")  # 字体文件

for k in range(780, 7542):  # 想要获取字体在文件中的范围
    names = font.getGlyphName(k)
    glyph = font.getGlyphSet()[names]
    coordinates = list(glyph._glyph.coordinates)
    endPts = glyph._glyph.endPtsOfContours
    flags = list(glyph._glyph.flags)

    lens = len(coordinates)

    savepath = "/Users/xiaomo/PycharmProjects/datause/excel" + str(k - 779) + ".xls"  # 保存文件名，从1开始
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('笔画信息', cell_overwrite_ok=True)
    j = 0
    for i in range(0, lens):
        sheet.write(i + j, 0, coordinates[i][0])
        sheet.write(i + j, 1, coordinates[i][1])
        sheet.write(i + j, 2, flags[i])
        if i in endPts:
            sheet.write(i + j + 1, 0, 9999)
            sheet.write(i + j + 1, 1, 9999)
            sheet.write(i + j + 1, 2, 9999)
            j = j + 1
    book.save(savepath)
    print(k)

# 需要自定义三个参数（字体文件，获取范围，保存文件名），每个笔画之间用（9999，9999，9999）隔开
