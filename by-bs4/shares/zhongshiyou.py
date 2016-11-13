import requests
from bs4 import BeautifulSoup
import os
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400'
}

url = 'http://quotes.money.163.com/trade/lsjysj_601857.html?year=2016&season=4'


# parameter
# shareCode/year/month : num ,
def sharesCrawl(shareCode,year,month):
    shareCodeStr = str(shareCode)
    yearStr = str(year)
    monthStr = str(month)
    url = 'http://quotes.money.163.com/trade/lsjysj_'+shareCodeStr+'.html?year='+yearStr+'&season='+monthStr

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    # print soup
    title = soup.select('h1.name > a')[0].get_text()

    date = soup.select('div.inner_box > table > tr > td')

    if os.path.exists('./'+shareCodeStr+title) == False:
        #create the share folder
        os.mkdir('./'+shareCodeStr+title)

    f = open('./'+shareCodeStr+title+'/Y'+yearStr+'S'+monthStr+'.txt','wb')
    for index,value in enumerate(date):
        if index % 11 == 10:
            f.write(value.get_text()+'\n')
        else:
            f.write(value.get_text() +'\t')
    f.close()

# sharesCrawl(600019,'2016','2')



def sharesCrawl2(shareCode,year,month):
    shareCodeStr = str(shareCode)
    yearStr = str(year)
    monthStr = str(month)
    url = 'http://quotes.money.163.com/trade/lsjysj_' + shareCodeStr + '.html?year=' + yearStr + '&season=' + monthStr
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    date = soup.select('div.inner_box > table > tr > td')
    resultString = ''
    for index, value in enumerate(date):
        if index % 11 == 10:
            resultString += value.get_text() + '\n'
        else:
            resultString += value.get_text() + '\t'
    return resultString

# print sharesCrawl2(600019,2016,2)



def createUrl(shareCode,beginYear,endYear):

    title = str(shareCode)

    if os.path.exists('./'+title) == False:
        #create the share folder
        os.mkdir('./'+title)

    f = open('./' + title + '.txt', 'wb')

    for i in range(beginYear,endYear+1):
        print i
        # time.sleep(5)
        for j in range(1,5):
            f.write(sharesCrawl2(shareCode,i,j) + '\n ------- '+str(i)+'/'+str(j)+'----------------\n')
            time.sleep(5)
    f.close()

createUrl(601857,2008,2016)


"""
body > div.area > div.inner_box > table > tbody > tr:nth-child(1) > td:nth-child(1)
body > div.area > div.header > div.stock_info > table > tbody > tr > td.col_1 > h1 > a
"""