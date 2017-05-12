# coding=utf-8
from __future__ import division
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import math


class ImageHandle:  # 直方图算法
    def __init__(self, img):
        img = 'app/static/upload/' + img
        self.img = Image.open(img)

    def ImageWay(self):
        size = (128, 128)
        image1 = self.img.resize(size).convert("RGB")
        data = image1.histogram()  # 获取图片直方图数据
        data = ImageHandle.turnStr(self, data)
        return data

    def AverageHash(self):  # 平均哈希算法
        size = (8, 8)
        pixel = []
        img = self.img.resize(size).convert('L')
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                pixel_value = img.getpixel((x, y))
                pixel.append(pixel_value)

        avg = sum(pixel) / len(pixel)

        cp = []

        for px in pixel:
            if px > avg:
                cp.append(1)
            else:
                cp.append(0)
        cp = ImageHandle.turnStr(self, cp)
        return cp

    def changeHash(self):  # 转换哈希算法
        size = (9, 8)
        img = self.img.resize(size).convert('L')
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
        result = ImageHandle.turnStr(self, result)
        return result

    def feelHash(self):  # 感知哈希算法
        size = (32, 32)
        part_size = (8, 8)
        img = self.img.resize(size).convert('L').filter(ImageFilter.BLUR)
        img = ImageOps.equalize(img)
        matrix = ImageHandle.get_matrix(self, img)
        DCT_matrix = ImageHandle.DCT(self, matrix)
        List = ImageHandle.sub_matrix_to_list(self, DCT_matrix, part_size)
        middle = ImageHandle.get_middle(self, List)
        code1 = ImageHandle.get_Haming(self, List, middle)
        code = ImageHandle.turnStr(self, code1)
        return code

    def get_matrix(self, image):
        matrix = []
        size = image.size
        for height in range(0, size[1]):
            pixel = []
            for width in range(0, size[0]):
                pixel_value = image.getpixel((width, height))
                pixel.append(pixel_value)
            matrix.append(pixel)

        return matrix

    def DCT(self, double_matrix):
        n = len(double_matrix)
        A = ImageHandle.get_coefficient(self, n)
        AT = ImageHandle.get_transposing(self, A)

        temp = ImageHandle.get_mult(self, double_matrix, A)
        DCT_matrix = ImageHandle.get_mult(self, temp, AT)

        return DCT_matrix

    def get_coefficient(self, n):
        matrix = []
        PI = math.pi
        sqr = math.sqrt(1 / n)
        value = []
        for i in range(0, n):
            value.append(sqr)
        matrix.append(value)

        for i in range(1, n):
            value = []
            for j in range(0, n):
                data = math.sqrt(2.0 / n) * math.cos(i * PI * (j + 0.5) / n)
                value.append(data)
            matrix.append(value)

        return matrix

    def get_transposing(self, matrix):
        new_matrix = []

        for i in range(0, len(matrix)):
            value = []
            for j in range(0, len(matrix[i])):
                value.append(matrix[j][i])
            new_matrix.append(value)

        return new_matrix

    def get_mult(self, matrix1, matrix2):
        new_matrix = []

        for i in range(0, len(matrix1)):
            value_list = []
            for j in range(0, len(matrix1)):
                t = 0.0
                for k in range(0, len(matrix1)):
                    t += matrix1[i][k] * matrix2[k][j]
                value_list.append(t)
            new_matrix.append(value_list)

        return new_matrix

    def sub_matrix_to_list(self, DCT_matrix, part_size):
        w, h = part_size
        List = []
        for i in range(0, h):
            for j in range(0, w):
                List.append(DCT_matrix[i][j])
        return List

    def get_middle(self, List):
        li = List
        li.sort()
        value = 0
        if len(li) % 2 == 0:
            index = int((len(li) / 2)) - 1

            value = li[index]
        else:
            index = int((len(li) / 2))
            value = (li[index] + li[index - 1]) / 2
        return value

    def get_Haming(self, List, middle):
        result = []
        for index in range(0, len(List)):
            if List[index] > middle:
                result.append("1")
            else:
                result.append("0")
        return result

    def turnStr(self, list):
        lens = len(list)
        i = 0
        s = ""
        while i < lens:
            s = s + str(list[i])
            i = i + 1
        return s


if __name__ == "__main__":
    print ImageHandle('1494560808.JPG').changeHash()
