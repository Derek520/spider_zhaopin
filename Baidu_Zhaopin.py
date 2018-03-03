# -*- coding:utf-8 -*-
import pandas
import requests,json
from User_agent import User_Agt

class BaiduZhaopin(object):
    '''招聘信息'''
    list1 = [] # 定义类属性,将提取的数据拼成字典放进list中
    count = 1
    def __init__(self):
        self.get_url ='http://zhaopin.baidu.com/api/quanzhiasync?'
        self.headers =User_Agt()
        self.city = '西安'
        self.name = 'python'
        self.pn = 0


    def get_data(self):
        '''准备数据'''
        self.pamans = {
            'query': self.name,
            'city': self.city,
            'pn': self.pn,
            'rn':20,
            'sort_type':1,
            'sort_key':5
        }
        # return pamans

    def get_url_list(self):
        '''获取url列表'''
        # 页码数

        data = requests.get(self.get_url,params=self.pamans,headers=self.headers)
        data_json = json.loads(data.content.decode())
        page = data_json['data']['main']['data']['dispNum']
        print(page)
        return [i*20 for i in range(38+1)]

    def pares_url(self):
        '''发送请求'''
        # 通过requests发送响应请求
        data = requests.get(self.get_url,params=self.pamans,headers = self.headers)
        print(data.url)
        # 将返回的数据进行解码，且转换成字典数据
        data_json = json.loads(data.content.decode())
        # print(data_json)
        # 返回数据
        return data_json


    def save_data(self,data):
        '''保存数据'''
        if not data['data']['main']['data']['listNum']:
            return None
        # 因为每页20条数据
        for q in range(20):

            try:
                # 拼成字典数据
                dict = {'公司名称': data['data']['main']['data']['disp_data'][q]['officialname'],
                        '所属行业': data['data']['main']['data']['disp_data'][q]['industry'],
                        '岗位名称': data['data']['main']['data']['disp_data'][q]['title'],
                        # '公司规模': data['data']['main']['data']['disp_data'][q]['ori_size'],
                        # '招聘人数': data['data']['main']['data']['disp_data'][q]['ori_number'],
                        '工资待遇': data['data']['main']['data']['disp_data'][q]['ori_salary'],
                        '岗位需求': data['data']['main']['data']['disp_data'][q]['description'],
                        '招聘网址': data['data']['main']['data']['disp_data'][q]['url'],
                        '发布时间': data['data']['main']['data']['disp_data'][q]['startdate'],
                        '结束时间': data['data']['main']['data']['disp_data'][q]['enddate']}
            except Exception as e:
                print()
                continue
            BaiduZhaopin.count +=1
            # 将每条字典数据，添加到类属性列表中
            BaiduZhaopin.list1.append(dict)


    def run(self):
        '''逻辑处理'''
        self.get_data()
        # 获取页码列表
        page = self.get_url_list()
        print(page)

        # 遍历每页数据
        for num in page:
            # 设置页码
            self.pamans['pn']=num
            print(self.pn)
            # 获取当前页数据
            # data = self.get_data()
            # 调用发送函数，发送请求相应
            resp = self.pares_url()
            # 随机产生一个用户代理
            self.header = User_Agt()
            # 调用保存数据方法，进行数据保存
            self.save_data(resp)
        print(BaiduZhaopin.count)
        # 当把所有页码遍历结束后，将数据保存成csv
        data1 = pandas.DataFrame(BaiduZhaopin.list1)
        data1.to_csv('最新招聘信息.csv',encoding='gb18030')



if __name__ == '__main__':

    baiduzp = BaiduZhaopin()
    baiduzp.run()
