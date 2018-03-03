# -*- coding:utf-8 -*-

import requests
from User_agent import User_Agt

class TiebaSpdider(object):

    def __init__(self,tiba_name):
        self.url_temp = 'https://tieba.baidu.com/f?kw='+ tiba_name +'&pn={}'
        self.headers = User_Agt()
        self.name = tiba_name
    def get_url_list(self):
        '''获取url列表'''
        return [self.url_temp.format(i*50) for i in range(1000)]


    def parse_url(self,url):
        '''发送请求,获取相应'''
        response = requests.get(url,headers=self.headers)
        return response.content


    def save_html(self,response,page):
        '''保存数据'''
        file_name = '{}第{}页.html'.format(self.name,page)
        with open(file_name,'wb') as f:
            f.write(response)


    def run(self):
        '''实现主要逻辑'''

        # 1.获取ur列表
        url_list = self.get_url_list()
        # 2.发送请求,获取响应
        for url in url_list:
            res = self.parse_url(url)


        # 3.保存
            index = url_list.index(url)
            self.save_html(res, index)
if __name__ == '__main__':

    tieba = TiebaSpdider('李毅')
    tieba.run()