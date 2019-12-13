#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import sys
import urllib.error as error
import urllib.request as request

'''
获取url中的图片
url：链接地址
dirpath：保存路径
'''


def getUrlImage(url, dirpath):
    dldNum = 0
    # 存储目录不存在时，创建目录
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)

    data = request.urlopen(url).read()
    page_data = data.decode('gbk', 'ignore')
    # 获取img标签数据
    page_image = re.compile('<img src=\"(.+?)\"')
    # 循环获取img标签中的图片
    for image in page_image.findall(page_data):
        # 匹配数据中的图片
        pattern = re.compile(r'^https://.*.(jpg|png|gif|jpeg)$')
        if pattern.match(image):
            print(image)
            try:
                extension = GetFileNameAndExt(image)
                # 读取图片内容
                image_data = request.urlopen(image).read()
                image_path = dirpath + '/' + str(dldNum) + extension
                dldNum += 1
                print(image_path)
                # 保存图片
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_data)
                    image_file.close()
            except error.URLError as e:
                print('Download failed')


'''
获取文件名中的扩展名
'''


def GetFileNameAndExt(filename):
    (filepath, tempfilename) = os.path.split(filename);
    (shotname, extension) = os.path.splitext(tempfilename);
    return extension


'''
入口函数
带两个参数
参数1:话题链接地址
参数2:图片保存路径
'''
if __name__ == "__main__":
    getUrlImage("https://www.zhihu.com/question/297715922/answer/512561486", "G:/OneDrive/zhihu/512561486")
