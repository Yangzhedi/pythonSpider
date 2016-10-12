# coding:utf-8
import requests
from bs4 import BeautifulSoup
import time

url = 'https://github.com/Ovilia?'
url2 = 'https://github.com/Ovilia?page={}&tab=following'
default_url = 'https://github.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
}

result_lists = []
is_go_on = True

def get_follow_lists(url,boo,pages = 1):
    # 组url
    true_url = url + 'page=' + str(pages) + '&tab=' + 'following' if boo else 'followers'
    data = requests.get(true_url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    lists = soup.select('div.d-table > div.d-table-cell > a.d-inline-block')
    if lists == []:
        print 'yaoxiugaiisgoon'
        is_go_on = False
        print is_go_on
    for i in lists:
        result_lists.append(default_url+i.get('href'))
        print default_url+i.get('href')
    print len(result_lists)

for i in range(1,10):
    if is_go_on:
        get_follow_lists(url,True,i)