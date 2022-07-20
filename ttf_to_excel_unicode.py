import xlwt
from fontTools.ttLib import TTFont

with open("unicode.txt", "r", encoding='UTF-8-sig') as f:  # 需求汉字unicode码的txt文件
    unis = f.readlines()
    aa = len(unis)

font = TTFont("kaitigb2312.ttf")  # 字体文件

for k in range(0, aa):
    uniss = str(unis[k])
    uniss = uniss.strip('\n')
    glyph = font.getGlyphSet()["uni" + str(uniss)]
    coordinates = list(glyph._glyph.coordinates)
    endPts = glyph._glyph.endPtsOfContours
    flags = list(glyph._glyph.flags)

    a = len(coordinates)

    savepath = "/Users/xiaomo/PycharmProjects/datause/excel" + str(uniss) + ".xls"  # 保存文件名，为unicode码
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('笔画信息', cell_overwrite_ok=True)
    j = 0
    for i in range(0, a):
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

# 需要自定义三个参数（字体文件，需求汉字unicode码的txt文件，保存文件名），每个笔画之间用（9999，9999，9999）隔开
