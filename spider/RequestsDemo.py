#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import os
import re


# 根据图片地址下载文档到本地
def download_picture(url, path):
    path = path + url.split("/")[-2]
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    data = response.content
    file = path + "/" + url.split("/")[-1]
    with open(file, "wb") as f:
        f.write(data)
        f.close()


# 根据页面地址，下载所有图片到本地
def download_allpicture(url, path):
    if not os.path.isdir(path):
        os.makedirs(path)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # response = requests.get(url)
    print(response.text)
    # 获取img标签数据
    page_image = re.compile('<img src=\"(.+?)\"')
    images = re.findall(page_image, response.text)
    for image in images:
        pattern = re.compile(r'^https://.*.(jpg|png|gif|jpeg)$')
        if pattern.match(image):
            print(image)
            image_dir = path + "/" + url.split("/")[-1]
            if not os.path.isdir(image_dir):
                os.makedirs(image_dir)
            image_dir = image_dir + "/" + image.split("/")[-1]
            with open(image_dir, "wb") as f:
                f.write(requests.get(image).content)
                f.close()


# 通过requests包下载单张网络图片到本地
# if __name__ == "__main__":
#     download_picture("https://pic3.zhimg.com/80/v2-19e9865fdfca0b0a1303ad691abb980c_hd.jpg",
#                      H:/照片/images/zhihu/request")

# 通过requests包下载多张网络图片到本地
if __name__ == "__main__":
    download_allpicture("https://www.zhihu.com/question/298912512", "H:/images/zhihu/request")
