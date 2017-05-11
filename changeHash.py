# coding=utf-8
from __future__ import division
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps


# 转换Hash算法，主要是根据明暗变换进行对比，对明暗的匹配精准，但是对颜色识别比较低
# 缩小图片：收缩到9*8的大小，以便它有72的像素点
# 转化为灰度图：把缩放后的图片转化为256阶的灰度图。（具体算法见平均哈希算法步骤）
# 计算差异值：dHash算法工作在相邻像素之间，这样每行9个像素之间产生了8个不同的差异，一共8行，则产生了64个差异值
# 获得指纹：如果左边的像素比右边的更亮，则记录为1，否则为0.最后比对两张图片的指纹，获得汉明距离即可。
# 最后结果，距离越小，越相似

def getCode(img, size):
    result = []
    x_size = size[0] - 1  # width
    y_size = size[1]  # high
    for x in range(0, x_size):
        for y in range(0, y_size):
            now_value = img.getpixel((x, y))
            next_value = img.getpixel((x + 1, y))

            if next_value < now_value:
                result.append(1)
            else:
                result.append(0)

    return result


def compCode(code1, code2):
    num = 0
    for index in range(0, len(code1)):
        if code1[index] != code2[index]:
            num += 1
    return num


def change_Hash(image1, image2, size=(9, 8)):
    image1 = image1.resize(size).convert('L')
    code1 = getCode(image1, size)

    image2 = image2.resize(size).convert('L')
    code2 = getCode(image2, size)

    assert len(code1) == len(code2), "error"
    res = compCode(code1, code2)
    res = ((72-res) / 72)
    return round(res, 2)


if __name__ == '__main__':
    img_1 = Image.open("testImage/test.jpg")
    img_2 = Image.open("testImage/testN.jpg")
    print change_Hash(img_1, img_2)
