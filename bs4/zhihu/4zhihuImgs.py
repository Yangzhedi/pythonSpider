import requests
import urllib
from bs4 import BeautifulSoup
import time

url = 'https://www.zhihu.com/question/47371654'

headers = {
    'User-Agent':'',  # your user-Agent here
    'Cookie':''    # your cookie here
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
imgs = soup.select('div.zm-editable-content > img')

img_link = []
folder_path = 'E://python/4weeks/jiandan/zhihuimg/'

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