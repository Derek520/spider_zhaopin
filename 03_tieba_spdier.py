# -*- coding:utf-8 -*-

import requests
from User_agent import User_Agt

class TiebaSpdider(object):
    def __init__(self,tiba_name):
        self.url_temp = 'https://tieba.baidu.com/f?kw='+ tiba_name +'&pn={}'
        self.headers = User_Agt()
    def get_url_list(self):
        '''获取url列表'''
        return [self.url_temp.format(i*50) for i in range(1000)]


    def parse_url(self,url):
        '''发送请求,获取相应'''
        response = requests.get(url,headers=self.headers)
        return response.content.decode()


    def save_html(self,response,page):
        '''保存数据'''
        file_name = '{}第{}页.html'.format(1,page)


    def run(self):
        '''实现主要逻辑'''

        # 1.获取ur列表
        url_list = self.get_url_list()
        # 2.发送请求,获取响应
        for url in url_list:
            respnose = self.parse_url(url)
        # 3.保存
        # page = url_list.index(url)+1
        # self.save_html(respnose,page)
if __name__ == '__main__':
    tieba = TiebaSpdider('李毅')