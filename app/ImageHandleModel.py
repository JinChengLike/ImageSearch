# coding=utf-8
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps


class ImageHandle:
    def __init__(self, img):
        self.img = img

    def ImageWay(self):
        size = (128, 128)
        image1 = self.img.resize(size).convert("RGB")
        data = image1.histogram()  # 获取图片直方图数据
        return data
