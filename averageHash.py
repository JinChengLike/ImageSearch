# coding=utf-8


#平均哈希法
# 1.缩放图片，可利用Image对象的resize(size)改变，一般大小为8*8，64个像素值。
# 2.转化为灰度图转灰度图的算法。
# 1.浮点算法：Gray=Rx0.3+Gx0.59+Bx0.11
# 2.整数方法：Gray=(Rx30+Gx59+Bx11)/100
# 3.移位方法：Gray =(Rx76+Gx151+Bx28)>>8;
# 4.平均值法：Gray=（R+G+B）/3;
# 5.仅取绿色：Gray=G；
# 在python中，可用Image的对象的方法convert('L')直接转换为灰度图
#
# 3.计算平均值：计算进行灰度处理后图片的所有像素点的平均值。
# 4.比较像素灰度值：遍历灰度图片每一个像素，如果大于平均值记录为1，否则为0.
# 5.得到信息指纹：组合64个bit位，顺序随意保持一致性。



from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps


def getHaming(img, size):     #获取图片的汉明距离
    pixel = []
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
    return cp


def compCode(code1, code2):        #对比返回两个图片的汉明距离
    num = 0
    for index in range(0, len(code1)):
        if code1[index] != code2[index]:
            num += 1
    return num


def aHash(image1, image2, size=(8, 8), exact=25):  #exact是我们自己设定的期望值，汉明距离小于该值我们就认为相似
    image1 = image1.resize(size).convert('L').filter(ImageFilter.BLUR)      #转换为灰度图
    image1 = ImageOps.equalize(image1)                    #计算像素点平均值
    code1 = getHaming(image1, size)
    image2 = image2.resize(size).convert('L').filter(ImageFilter.BLUR)
    image2 = ImageOps.equalize(image2)
    code2 = getHaming(image2, size)

    assert len(code1) == len(code2), "error"

    return compCode(code1, code2) <= exact


if __name__ =='__main__':
    img_1 = Image.open("testImage/test.jpg")
    img_2 = Image.open("testImage/test4.jpg")
    print aHash(img_1,img_2)
