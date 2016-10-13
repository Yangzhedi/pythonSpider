# coding:utf-8
import requests
from bs4 import BeautifulSoup
import time

url = 'https://github.com/'
default_url = 'https://github.com'
headers = {
    'User-Agent': '' # ur user-Agent here
}

result_lists = []

def counts2pages(Tag):
    str = Tag.get_text().replace(' ','').strip('\n').encode('utf-8')
    leng = len(str)-1
    if str[-1] == 'k':
        pages = int(float(str[:leng]) * 1000)/51 + 1
    else:
        pages = int(str)/51 + 1
    return pages


def get_follow_counts_pages(url,person,boo):
    followXXX = 'following' if boo else 'followers'
    true_url = url + person + '?tab=' + followXXX
    data = requests.get(true_url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    counts = soup.select('div.user-profile-nav > nav > a.underline-nav-item > span')
    # 如果boo 是真，说明是following ，counts[3]
    if boo:
        return counts2pages(counts[3])
    else:
        return counts2pages(counts[2])

def get_follow_lists(url,person,boo,pages = 1):
    # 组url
    followXXX = 'following' if boo else 'followers'
    true_url = url + person + '?page=' + str(pages) + '&tab=' + followXXX
    data = requests.get(true_url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    lists = soup.select('div.d-table > div.d-table-cell > a.d-inline-block')
    if lists == []:
        print 'yaoxiugaiisgoon'
    for i in lists:
        result_lists.append(default_url+i.get('href'))
        print default_url+i.get('href')
    print len(result_lists)
    return result_lists

for i in range(1,10):
    get_follow_lists(url,'ruanyf',True,i)