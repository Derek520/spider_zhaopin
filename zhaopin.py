# -*- coding:utf-8 -*-
import requests,json
from User_agent import User_Agt
import pandas

class BaiduZhaopin(object):
    '''百度招聘'''
    list1 = []
    def __init__(self):
        self.url = None
        self.user_agt = User_Agt()


    def get_url(self):
        '''请求数据'''
        data = requests.get(self.url,headers=self.user_agt)
        data_str = data.content.decode()
        data_json = json.loads(data_str)
        return data_json

    def save_data(self,data):
        '''保存数据'''
        for q in range(20):
            try:
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
                print('----{}数据异常---网址：{}'.format(e,self.url))
                continue

            BaiduZhaopin.list1.append(dict)


    def run(self):
        '''逻辑处理'''
        city_list = ['北京', '上海', '深圳', '杭州', '广东', '西安', '郑州']

        for city in city_list:
            print(city)
            for page in range(0,760,20):
                # 1.获取发送的数据
                self.url ='http://zhaopin.baidu.com/api/quanzhiasync?query=python&sort_key=5&sort_type=1&city='+ city +'&detailmode=close&rn=20&pn={}'.format(page)
                # 2.请求响应
                res_data = self.get_url()
                # 3.保存数据
                self.save_data(res_data)

        save_data = pandas.DataFrame(BaiduZhaopin.list1)
        save_data.to_csv('全部招聘.csv',encoding='gb18030')



if __name__ == '__main__':
    bz = BaiduZhaopin()
    bz.run()


