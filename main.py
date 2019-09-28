'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/14 9:15
@Software: PyCharm
@File    : main.py
'''
import requests
from lxml import etree

# 1、将目标网站上的页面爬取下来
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ('
#                   'KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 '
#                   'Core/1.70.3650.400 QQBrowser/10.4.3341.400',
#     'Referer': 'https://movie.douban.com/'
# }
# url = 'https://movie.douban.com/cinema/nowplaying/taian/'
# response = requests.get(url,headers=headers)
# print(response.text)
#response.text:返回的是一个经过解码后的字符串，是str（unicode）类型
#response.content：返回的是一个原生字符串，从网页上抓取下来没有经过处理的字符串，
#是bytes类型
# with open('douban.html','w',encoding='utf-8') as f:
#     f.write(response.text)

#2、将抓取下来的数据根据一定规则进行提取
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('douban.html',parser=parser)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    release = li.xpath("@data-release")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    votecount = li.xpath("@data-votecount")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title':title,
        'score':score,
        'release':release,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'votecount':votecount,
        'thumbnail':thumbnail
    }
    movies.append(movie)
print(movies)