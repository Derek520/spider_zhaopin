# -*- coding:utf-8 -*-

import requests
import json
import sys

'''
query:人生苦短
from:zh
to:en
'''

url = 'http://fanyi.baidu.com/basetrans'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}


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

    def __init__(self, query_string):
        self.post_url = 'http://fanyi.baidu.com/basetrans'
        self.query_string = query_string

    def get_post_data(self):
        '''准备post数据'''
        data = {
            'query': self.query_string,
            'from': 'zh',
            'to': 'en'
        }
        return data

    def parse_url(self, post_data):
        '''发送数据'''
        res = requests.post(self.post_url, data=post_data, headers=headers)
        return res.content.decode()

    def get_ret(self, html_str):
        '''提取数据'''
        data_dict = json.loads(html_str)
        return data_dict['trans'][0]['dst']

    def save_info(self):
        '''保存数据'''
        pass

    def run(self):
        '''实现逻辑'''
        # 准备表单数据
        post_data = self.get_post_data()
        # 请求响应
        html_str = self.parse_url(post_data)
        # 提取数据
        data_dict = self.get_ret(html_str)

        print(data_dict)

if __name__ == '__main__':
    print(sys.argv)
    data = sys.argv[1]
    fy = BaiduFanyi(data)
    fy.run()