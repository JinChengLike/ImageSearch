# coding=utf-8
from __future__ import division
from PIL import Image


# 直方算法进行匹配度计算
# 通过.histogram()方法获取图片颜色空间的直方数据
# 循环判断，遍历所有像素的颜色空间值，相同记为一，不相同通过注释的公式进行计算，存在列表中
# 整个列表的求平均获取相似值，越接近一越相似

def classfiy_histogram(image1, image2, size=(128, 128)):
    image1 = image1.resize(size).convert("RGB")
    g = image1.histogram()  # 获取图片直方图数据

    image2 = image2.resize(size).convert("RGB")
    s = image2.histogram()

    assert len(g) == len(s), "error"

    data = []

    for index in range(0, len(g)):
        if g[index] != s[index]:
            r = 1 - abs(g[index] - s[index]) / max(g[index], s[index])  # 颜色空间不同，计算公式
            data.append(round(r, 4))
        else:
            data.append(1)
    res = sum(data) / len(g)
    return round(res, 4)


if __name__ == '__main__':
    img_1 = Image.open("testImage/test.jpg")
    img_2 = Image.open("testImage/test4.jpG")
    print classfiy_histogram(img_1, img_2)
