import cv2
import numpy as np
import random
import os

z = 0
for k in range(1, 24):
    f = open("/Users/xiaomo/PycharmProjects/datause/strokes-classify-number/" + str(k) + ".txt", "r")
    lines = f.readlines()
    aa = len(lines)

    for line in lines:
        x = line.rstrip('\n')
        img = cv2.imread("/Users/xiaomo/PycharmProjects/datause/imageall/28/" + str(x) + ".png", 1)
        for y in range(0, 1200):
            a = random.uniform(-9, 9)
            b = random.uniform(0.90, 1.10)
            c = random.randint(-2, 2)
            d = random.randint(-2, 2)
            imgInfo = img.shape
            height = imgInfo[0]
            width = imgInfo[1]
            mode = imgInfo[2]
            matRotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), a, b)
            # 参数1:需要旋转的中心点.参数2:需要旋转的角度.参数三:需要缩放的比例.

            dst = cv2.warpAffine(img, matRotate, (height, width))
            dst1 = np.zeros(imgInfo, np.uint8)
            dst2 = np.zeros(imgInfo, np.uint8)
            for i in range(height):
                for j in range(width - abs(c)):
                    dst1[i, j + c] = dst[i, j]
            for i in range(height - abs(d)):
                for j in range(width):
                    dst2[i + d, j] = dst1[i, j]
            # dst3 = cv2.resize(dst2, (28, 28), interpolation=cv2.INTER_AREA)  # 修改图片像素长度
            dir_name = '/Users/xiaomo/PycharmProjects/dataset/28/'
            os.makedirs(dir_name + str(k), exist_ok=True)
            os.makedirs(dir_name + str(k) + "/" + str(x), exist_ok=True)
            cv2.imwrite(dir_name + str(k) + "/" + str(x) + "/" + str(x) + "_" + str(y + 1) + ".png", dst2)
        z = z + 1
        print(z)
# 需要定义四个参数（笔画范围，原图位置，修改图片像素长度，文件保存位置），可调四个参数：a旋转角度（°），b放缩比例，c横坐标平移，d纵坐标平移
