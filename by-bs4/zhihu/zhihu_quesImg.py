# coding:utf-8
import requests
import urllib
from bs4 import BeautifulSoup
import time
import os


quesNumStr = str(input("请输入问题数字："))


url = 'https://www.zhihu.com/question/'+quesNumStr

headers = {
    'User-Agent':'',  # your user-Agent here
    'Cookie':''    # your cookie here
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
imgs = soup.select('div.zm-editable-content > img')
title = soup.select('#zh-question-title > h2 > span')[0].get_text()

img_link = []
folder_path = './'+title+'/'
if os.path.exists(folder_path) == False:
    # create the image folder
    os.mkdir(folder_path)

for i in imgs:
    img_link.append(i.get('data-actualsrc'))
    # print i.get('data-actualsrc')

# if folder_path == False:
#     open(folder_path,'wr')
print title
print str(len(img_link))+'张图片'

for index,item in enumerate(img_link):
    urllib.urlretrieve(item, folder_path + str(index)+'.jpg')
    print 'Done'+ str(index)
    time.sleep(4)