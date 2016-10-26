# coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list4']
item_info = ceshi['item_info4']

# 获取每一项下具体的url
def get_links_from(channel, pages, who_sells=0):
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            item_title = link.get_text()
            # print link.get('href')      # http://zhuanzhuan.58.com/detail/774777200171630596z.shtml?fullCate=5%2C36&fullLocal=1&from=pc
            # print item_link             # http://zhuanzhuan.58.com/detail/774777200171630596z.shtml
            url_list.insert_one({'url': item_link, 'title': item_title})
            print item_link,item_title
            if item_link != 'http://jump.zhineng.58.com/jump':
                get_item_info(item_link)
    else:
        pass

# 获取每一页的具体信息
def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('link',type="text/css").get('href').split('/')
    if no_longer_exist:
        pass
    else:
        title_soup = soup.title.text
        title = title_soup.split('_')[0]
        user = title_soup.split('_')[1].split('-')[0].split('的闲置物品')[0]
        price = soup.select('span.price_now i')[0].text
        area = soup.select('.palce_li span i')[0].text # if soup.find_all('span', 'c_25d') else None
        item_info.insert_one({'title': title, 'price': price, 'area': area, 'url': url, 'user': user})
        print {'title': title, 'price': price, 'area': area, 'user': user}
