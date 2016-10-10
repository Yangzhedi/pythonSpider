import requests
import urllib
from bs4 import BeautifulSoup
import time

url = 'https://www.zhihu.com/question/47371654'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
    'Cookie':''    # your cookie hear
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
imgs = soup.select('div.zm-editable-content > img')

img_link = []
folder_path = 'E://python/4weeks/jiandan/zhihuluoliimg/'

for i in imgs:
    img_link.append(i.get('data-actualsrc'))
    # print i.get('data-actualsrc')

# if folder_path == False:
#     open(folder_path,'wr')
print len(img_link)

for index,item in enumerate(img_link):
    urllib.urlretrieve(item, folder_path + str(index)+'.jpg')
    print 'Done'+ str(index)
    time.sleep(4)