# -*- coding:utf-8 -*-

import requests
import json
import sys,re

'''
query:人生苦短
from:zh
to:en
'''

url = 'http://fanyi.baidu.com/basetrans'
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}


# data={
#     'query': '大笨蛋',
#     'from':'zh',
#     'to':'en'
# }
# res =requests.post(url,data=data,headers=headers)
#
# data = json.loads(res.content.decode())
# print(data['trans'][0]['dst'])

class BaiduFanyi(object):
    '''百度翻译'''

    def __init__(self, query_string,lang):
        self.post_url = 'http://fanyi.baidu.com/basetrans'
        self.langde = 'http://fanyi.baidu.com/langdetect'
        self.headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}

        self.query_string = query_string

        self.lang = lang

    def get_post_data(self,lan):
        '''准备post数据'''
        # if lan == 'zh':
        #     data = {
        #         'query': self.query_string,
        #         'from': 'kor',
        #         'to': lan
        #     }
        #     return data
        #
        # if lan == 'en':
        #     data = {
        #         'query': self.query_string,
        #         'from': 'en',
        #         'to': lan
        #     }
        #     return data

        data = {
            'query': self.query_string,
            'from': lan,
            'to': self.lang
        }
        return data

    def parse_url(self, post_data):
        '''发送数据'''
        print(post_data)
        res = requests.post(self.post_url, data=post_data, headers=headers)
        print(res.content.decode())
        return res.content.decode()

    def langList(self):
        '''langList'''
        print(123)
        lang_url = 'http://fanyi.baidu.com/'
        res_lang = requests.get(lang_url,headers=self.headers)
        # with open('111.html','wb') as f:
        #     f.write(res_lang.content)
        data =res_lang.content.decode()


        comp = re.compile(r'langList: {(.*?)},',re.S)
        data = comp.findall(data)
        for mm in data:
            print(mm)


    def langdet(self):
        '''判断是什么语言'''
        ''''''
        data = {
            'query': self.query_string
        }
        res_data = requests.post(self.langde,data=data,headers = self.headers)

        data = json.loads(res_data.content.decode())['lan']


        return data

    def get_ret(self, html_str):
        '''提取数据'''
        data_dict = json.loads(html_str)
        return data_dict['trans'][0]['dst']

    def save_info(self):
        '''保存数据'''
        pass

    def run(self):
        '''实现逻辑'''

        lan = self.langdet()
        # 准备表单数据
        post_data = self.get_post_data(lan)

        # 请求响应
        html_str = self.parse_url(post_data)
        # 提取数据
        data_dict = self.get_ret(html_str)

        print(data_dict)

if __name__ == '__main__':
    print(sys.argv)
    data = sys.argv[1]
    lang = sys.argv[2]
    print(data,lang)
    fy = BaiduFanyi(data,lang)
    fy.run()
