# coding=utf-8
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps


class ImageCheckModel:
    def checkByImageWay(self,img1,img2):
        assert len(img1) == len(img2), "error"

        data = []

        for index in range(0, len(img1)):
            if img1[index] != img2[index]:
                r = 1 - abs(img1[index] - img2[index]) / max(img1[index], img2[index])  # 颜色空间不同，计算公式
                data.append(round(r, 4))
            else:
                data.append(1)
        res = sum(data) / len(img1)
        return round(res, 4)