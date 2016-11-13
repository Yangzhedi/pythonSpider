import requests
from bs4 import BeautifulSoup
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400'
}

url = 'http://quotes.money.163.com/trade/lsjysj_601857.html?year=2016&season=4'

def sharesCrawl(shareCode,year,month):

    url = 'http://quotes.money.163.com/trade/lsjysj_'+shareCode+'.html?year='+year+'&season='+month

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    # print soup
    title = soup.select('h1.name > a')[0].get_text()

    date = soup.select('div.inner_box > table > tr > td')

    if os.path.exists('./'+shareCode+title) == False:
        #create the share folder
        os.mkdir('./'+shareCode+title)

    f = open('./'+shareCode+title+'/Y'+year+'S'+month+'.txt','wb')
    for index,value in enumerate(date):
        if index % 11 == 10:
            f.write(value.get_text()+'\n')
        else:
            f.write(value.get_text() +'\t')
    f.close()

sharesCrawl('601600','2016','2')


"""
body > div.area > div.inner_box > table > tbody > tr:nth-child(1) > td:nth-child(1)
body > div.area > div.header > div.stock_info > table > tbody > tr > td.col_1 > h1 > a
"""