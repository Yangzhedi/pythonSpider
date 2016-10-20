# coding:utf-8
import requests
from bs4 import BeautifulSoup
from github_followXXXList import count
import time

url = 'https://github.com/'

headers = {
    'User-Agent': '' #  ur user-Agent here,
}

def get_user_info(url,person):
    data = requests.get(url + person, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    name = soup.select('div > div.vcard-names-container.py-3.js-sticky. > h1 > span.vcard-fullname')
    intrduction = soup.select('div.user-profile-bio > div')
    counts = soup.select('div.user-profile-nav > nav > a.underline-nav-item > span')
    dic = {
        'name':name[0].get_text(),
        'intrduction':intrduction[0].get_text(),
        'repsoitories_count': count(counts[0]),
        'followers_count': count(counts[2]),
        'following_count': count(counts[3]),
        'post_star':count(counts[1]),
    }
    return dic
