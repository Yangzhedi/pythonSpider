import requests
import urllib
from bs4 import BeautifulSoup
import time
import string

url = 'https://github.com/Ovilia'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
print soup.prettify()
langs = soup.select(' ol.pinned-repos-list > li > span.pinned-repo-item-content > p.text-gray.mb-0')
for i in langs:
    print i.get_text().replace(' ','').strip('\n')