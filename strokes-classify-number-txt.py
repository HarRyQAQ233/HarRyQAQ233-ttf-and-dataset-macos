import xlrd

f = open("3755.txt", "r")  # 汉字序号文件
lines = f.readlines()
for line in lines:
    a = line.rstrip('\n')
    print(a)  # 汉字序号
    workBook = xlrd.open_workbook('/Users/xiaomo/PycharmProjects/datause/excel/' + str(a) + '.xls')
    h = a
    sheet1_content1 = workBook.sheet_by_index(0)
    nrows = sheet1_content1.nrows  # 行数

    k = 0

    for i in range(0, nrows):
        if sheet1_content1.cell(i, 0).value == 9999:
            k = k + 1

    print(k)  # 汉字笔画数
    
    os.makedirs("/Users/xiaomo/PycharmProjects/datause/strokes-classify-number/", exist_ok=True)
    with open('/Users/xiaomo/PycharmProjects/datause/strokes-classify-number/' + str(k) + '.txt', 'a', encoding='utf-8') as f:
        f.write(h + '\n')

#  需要自定义两个参数（汉字序号文件，excel文件位置），可获得汉字序号和笔画数
