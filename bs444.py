# -*- coding:utf-8 -*-
import bs4
from bs4 import BeautifulSoup

import requests
from lxml import etree

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}

try:
    response = requests.get(url, headers=headers)
    resHtml = response.text

    html = etree.HTML(resHtml)
    result = html.xpath('//div[contains(@id,"qiushi_tag")]')
    print(result)

    for site in result:
        print(site)
        item = {}

        imgUrl = site.xpath('./div/a/img/@src')[0].encode('utf-8')
        username = site.xpath('./div/a/@title')[0].encode('utf8')
        #username = site.xpath('.//h2')[0].text
        content = site.xpath('.//div[@class="content"]/span')[0].text.strip().encode('utf-8')
        # 投票次数
        vote = site.xpath('.//i')[0].text
        #print site.xpath('.//*[@class="number"]')[0].text
        # 评论信息
        comments = site.xpath('.//i')[1].text

        print(imgUrl, username.decode(), content.decode(), vote, comments)

except Exception as e:
    print(e)