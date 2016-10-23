# coding:utf-8
# 爬取豆瓣电影短评
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib
from bs4 import BeautifulSoup
import time

url = 'https://movie.douban.com/subject/26683290/comments'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'lxml')
# users:用户列表    comments:评论列表
count = soup.select('#content > div > div.article > div.title_line.clearfix.color_gray > span.fleft')
users = soup.select('div.comment > h3 > span.comment-info > a')
comments = soup.select('#comments > div.comment-item > div.comment > p')

# print count[0].get_text().split('全部共')[1].split('条')[0]
# print comments[4].get_text().strip().replace('\n',' ')
f = open('./text.txt','wb')
f.write(count[0].get_text()+'\n')
for index,item in enumerate(comments):
    print users[index].get_text() + ':' + item.get_text().strip().strip('\n')+'\n'
    f.write(users[index].get_text() + ':' + item.get_text().strip().replace('\n',' ')+'\n\n')
f.close()