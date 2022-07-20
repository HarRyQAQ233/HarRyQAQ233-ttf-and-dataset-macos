import xlrd
import cv2
import numpy as np
import os

f = open("6763.txt", "r")
lines = f.readlines()
for z in lines:
    z = z.rstrip('\n')
    workBook = xlrd.open_workbook('/Users/xiaomo/PycharmProjects/datause/excel/' + str(z) + '.xls')
    h = z
    sheet1_content1 = workBook.sheet_by_index(0)
    nrows = sheet1_content1.nrows  # 行数

    l = -1  # 过渡每个笔画中间值
    k = 0  # 记录笔画数
    strokes = []  # 存储每个笔画点数据
    images = []  # 存储每个笔画图数据
    for i in range(0, nrows):
        if sheet1_content1.cell(i, 0).value == 9999:

            img = np.zeros((257, 257, 3), np.uint8)  # 点范围为（0，256），所以设置257为图片边界宽度

            points = ([[int(sheet1_content1.cell(i - 1, 0).value), 220 - int(sheet1_content1.cell(i - 1, 1).value)]])
            # 把每组最后一个点放入数组

            for j in range(l + 1, i - 1):
                cv2.line(img, (int(sheet1_content1.cell(j, 0).value), 220 - int(sheet1_content1.cell(j, 1).value)),
                         (int(sheet1_content1.cell(j + 1, 0).value),
                          220 - int(sheet1_content1.cell(j + 1, 1).value)), (255, 255, 255), 1)

                points.append([int(sheet1_content1.cell(j, 0).value), 220 - int(sheet1_content1.cell(j, 1).value)])
                # 添加每个点进入数组

            cv2.line(img, (int(sheet1_content1.cell(i - 1, 0).value), 220 - int(sheet1_content1.cell(i - 1, 1).value)),
                     (int(sheet1_content1.cell(l + 1, 0).value),
                      220 - int(sheet1_content1.cell(l + 1, 1).value)), (255, 255, 255), 1)  # 220 = - 36 +256，-36是ymin

            area = np.array(points)
            cv2.fillPoly(img, [area], (255, 255, 255))

            strokes.append(points)
            images.append(img)
            k = k + 1
            l = i

    os.makedirs("/Users/xiaomo/PycharmProjects/datause/imagelack/28/", exist_ok=True)

    imgall = np.zeros((257, 257, 3), np.uint8)

    for x in range(0, k):
        imgall = imgall + images[x]

    for x in range(0, k):
        imglack = imgall - images[x]
        imglack1 = cv2.resize(imglack, (28, 28), interpolation=cv2.INTER_AREA)  # 修改图片像素长度
        cv2.imwrite("/Users/xiaomo/PycharmProjects/datause/imagelack/28/" + str(h) + "no" + str(x + 1) + ".png",
                    imglack1)  # 保存汉字缺少每一笔笔画图像
    print(z)

#  需要自定义三个参数（需读取excel文件位置，图片保存位置和名称，修改图片像素长度），可获得汉字笔画数k
