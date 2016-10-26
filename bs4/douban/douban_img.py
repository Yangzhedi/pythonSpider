import requests
import urllib
from bs4 import BeautifulSoup
import time
import os

url = 'https://movie.douban.com/chart'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
imgs = soup.select(' div > div > table > tr > td > a > img')

img_link = []
folder_path = './img/'

if os.path.exists(folder_path) == False:
    os.makedirs(folder_path)

for i in imgs:
    # print i.get('src')
    img_link.append(i.get('src'))

for index,item in enumerate(img_link):
    urllib.urlretrieve(item, folder_path + str(index)+'.jpg')
    print 'Done'+ str(index)
    time.sleep(4)