import requests
import urllib
from bs4 import BeautifulSoup
import time

url = 'https://www.zhihu.com/question/47371654'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
    'Cookie':'_zap=fdc10f33-9395-4fbe-83c3-27ab1b6ac42c; _za=52627d46-2b3b-42e8-a01a-d82a65ef3af1; udid="ABCAsoPamwmPTqZ-TGOXIieqtFNmzGeNZXM=|1457857978"; d_c0="AIDA4_zbsQmPTlm_GxHotmNmMDlO55_h4LQ=|1459334759"; _zap=75dd1e75-e521-4496-9ada-80af7899d1e3; q_c1=6516fcfb451c438eaa04846a11d66ac3|1475072605000|1444492773000; _xsrf=c796adc5f9c6a3a1c2edb81a5fd5fe9d; l_cap_id="MGVkZTVjZTc0OTBkNDdjZWIzYjFiZWM1YThiN2VlM2Q=|1475834204|b5c055bf73cc0fdc206bbb535e998eee8eaf735c"; cap_id="NDA3MDk5NDZkYzdlNGRkNmFkZGQ1NjlhMDg0MjdlNGU=|1475834204|f17e8399a5ad8346025a8e2550798f1e0dceb73e"; login="YzYxYmRhYmQ0Y2EyNDcyZDgzMzk1NGM1NjZiYzZjZTg=|1475834209|8e09bbfaba596cbb40a765634ca0a2b52ab72e13"; n_c=1; s-q=%E9%92%93%E9%B1%BC; s-i=2; sid=jdaa4fk8; s-t=autocomplete; __utma=51854390.2084936069.1475912182.1475912182.1475912182.1; __utmb=51854390.15.9.1475912497176; __utmc=51854390; __utmz=51854390.1475912182.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20140501=1^3=entry_date=20140501=1; a_t="2.0AABA1LktAAAXAAAAwzAgWAAAQNS5LQAAAIDA4_zbsQkXAAAAYQJVTWL-HlgAHr_iby7jOKVyxYosx5VIq80wLb-LSbqZZMDzSnqWHtTlJpAVlRu-4w=="; z_c0=Mi4wQUFCQTFMa3RBQUFBZ01Eal9OdXhDUmNBQUFCaEFsVk5ZdjRlV0FBZXYtSnZMdU00cFhMRmlpekhsVWlyelRBdHZ3|1475912643|ab78a790f02c26bc3461df5d3a2b85fad78391a3'
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