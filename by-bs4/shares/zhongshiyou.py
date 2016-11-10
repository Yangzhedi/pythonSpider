import requests
from bs4 import BeautifulSoup

url = 'http://quotes.money.163.com/trade/lsjysj_601857.html?year=2016&season=3'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400'
}

data = requests.get(url , headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
# print soup
date = soup.select('div.inner_box > table > tr > td')

f = open('./Y2016S3.txt','wb')
for index,value in enumerate(date):
    print value.get_text(),index
    if index % 11 == 10 :
        f.write(value.get_text()+'\n')
    else:
        f.write(value.get_text() +'\t')
f.close()

"""
body > div.area > div.inner_box > table > tbody > tr:nth-child(1) > td:nth-child(1)
"""