# coding:utf-8
import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.zhihu.com/people/mu-tong-63'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.95 Safari/537.36 Core/1.50.1414.400 QQBrowser/9.5.9244.400' #  ur user-Agent here,
}

def list_is_none_and_get_text(list,index):
    if list:
        return list[index].get_text()
    else:
        return None

def get_user_info(url):
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    name = list_is_none_and_get_text(soup.select('div > div.top > div.title-section > span'),0)
    sex = soup.select('div > span.info-wrap > span.item.gender > i')[0]['class'][1].split('-')[2]
    address = soup.select('span.info-wrap > span.location.item')[0]['title']
    agree = list_is_none_and_get_text(soup.select('div > span.zm-profile-header-user-agree > strong'),0)
    thanks = list_is_none_and_get_text(soup.select('div > span.zm-profile-header-user-thanks > strong'),0)
    followees = list_is_none_and_get_text(soup.select('div.zm-profile-side-following.zg-clear > a > strong'),0)
    followers = list_is_none_and_get_text(soup.select('div.zm-profile-side-following.zg-clear > a > strong'),1)
    employment = list_is_none_and_get_text(soup.select('div.items > div > span.info-wrap > span.employment.item > a'),0)
    content = list_is_none_and_get_text(soup.select('span.info-wrap.fold-wrap.fold.disable-fold > span.fold-item > span'),0).strip('\n')
    dic = {
        'name': name,
        'sex': sex,
        'address': address,
        'agree': agree,
        'thanks': thanks,
        'followees': followees,
        'followers': followers,
        'employment': employment,
        'content': content,
    }
    print dic
    return dic
# get_user_info(url)
