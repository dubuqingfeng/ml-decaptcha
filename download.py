#!/usr/bin/python
import requests
from PIL import Image
from PIL import ImageEnhance
import pytesseract


def download_pic(i):
    url = "http://jwxt.sxau.edu.cn/validateCodeAction.do?random=0.9090956765673528"
    r = requests.get(url, stream=True)
    with open('pics/%04d.jpg' % i, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)


def process_pic(i):
    im = Image.open('pics/%04d.jpg' % i)
    # 图像增强
    # im = ImageEnhance.Sharpness(im).enhance(3)
    # 灰度化
    convert_img = im.convert('L')
    convert_img.save('output_pics/%04d.jpg' % i)
    # 二值化
    threshold = 120
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    out = convert_img.point(table, '1')
    out = depoint(out)
    out.save('out_pics/%04d.jpg' % i)


def depoint(img):
    pixdata = img.load()
    w,h = img.size
    for y in range(1, h-1):
        for x in range(1, w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img


def print_result(i):
    print(''.join(pytesseract.image_to_string(Image.open('out_pics/%04d.jpg' % i), lang='eng', config='-psm 7').split()))


if __name__ == '__main__':
    for i in range(20):
        download_pic(i)
        process_pic(i)
        print_result(i)