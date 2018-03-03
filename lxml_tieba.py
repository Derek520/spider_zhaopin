# -*- coding:utf-8 -*-
from lxml import etree
import requests,os
from  User_agent import User_Agt

class TieBa(object):
    '''贴吧'''
    def __init__(self):
        self.tiebaName = input("请需要访问的贴吧：")
        self.beginPage = int(input("请输入起始页："))
        self.endPage = int(input("请输入终止页："))
        self.num =1
        self.url = 'http://tieba.baidu.com/f?'
        self.headers =User_Agt()

    def run(self):
        '''获取页码'''
        print('run')
        for page in range(self.beginPage,self.endPage+1):
            pn = (page - 1) * 50  # page number
            word = {'pn': pn, 'kw': self.tiebaName}
            self.read_url(word)

    def read_url(self,word):
        '''读取页面'''
        print('read_url')
        html = requests.get(self.url,params=word,headers =self.headers)
        html =html.text
        selector = etree.HTML(html)
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in links:
            link = "http://tieba.baidu.com" + link
            self.image_url(link)


    def image_url(self,image_url):
        '''图片链接'''
        print('image_url')
        html= requests.get(image_url,headers=self.headers)
        html=html.text
        selector = etree.HTML(html)

        imagesLinks = selector.xpath('//img[@class="BDE_Image"]/@src')

        for image in imagesLinks:
        #     保存图片
            self.save_image(image)

    def save_image(self,image):
        '''保存图片'''
        print("正在存储文件 %d ..." % self.num)
        image = requests.get(image,headers=self.headers)

        file_path = os.path.join('tieba/%s.jpg' % self.num)

        with open(file_path,'wb') as f:
            f.write(image.content)

        self.num +=1

if __name__ == '__main__':
    tieba =TieBa()
    tieba.run()

