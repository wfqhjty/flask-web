import re

# page_image = re.compile('<img src=\"(.+?)\"')
# images = re.findall(page_image, "<img src=\"aaaaaa\"bbbbbbbbbbb<img src=\"cccccc\"")
# for image in images:
#     print(image)

# pattern = re.compile(r'^https://.*.(jpg|png|gif|jpeg)$')
# # str = "https://1111.1jpg"
# # if pattern.match(str):
# #     print("true")
# # else:
# #     print("false")

# pattern = re.compile('abb\\.')
# str = 'abb.'
# if pattern.match(str):
#     print("true")
# else:
#     print("false")

import os

path = os.getcwd()
files = os.listdir(path)
listdir = []
for file in files:
    print(file)
    file = os.path.join(path, file)
    listdir.append(file)
print(listdir)

content = ""
for file in listdir:
    print(file)
    cc = open(file, 'r', encoding='utf8')
    content += cc.read()
    print(content)

with open(os.path.join(path, "1.txt"), 'w', encoding='utf8') as f:
    f.write(content)
    f.close()
