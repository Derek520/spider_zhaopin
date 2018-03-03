# -*- coding:utf-8 -*-
import requests,re
from User_agent import User_Agt
import json
import pandas# 使用pandas存数据

wb = {'query':'python','city_sug':"北京"}
city_list = ['北京','上海','深圳','杭州','广东','西安','郑州']

url = 'http://zhaopin.baidu.com/quanzhi?'

url2 = 'http://zhaopin.baidu.com/api/quanzhiasync?query=python&sort_key=5&sort_type=1&city=%E5%8C%97%E4%BA%AC&detailmode=close&rn=20&pn='

# header = User_Agt()
#
# res = requests.get(url,params=wb,headers = header)
#
# data = res.content.decode()
#
# pattern = re.compile(r'<div class="title-h3 line-clamp1"><span>(.*?)</span></div>', re.S)
# price = re.compile(r'<p class="area line-clamp1">(.*?)</p>',re.S)
# url_list = re.compile(r'<a class="clearfix item line-bottom" target="_blank" href=\'/szzw\?detailidx=0&city=北京(.*?)>',re.S)
# list1 = pattern.findall(data)
# list2 = price.findall(data)
# zw = url_list.findall(data)
# print(zw)
# # 拼接岗位职责页面
# url_one = url2+zw[0]
# # 从新请求
# data2 = requests.get(url_one,headers=header)
# data2 =data2.content.decode()
# # 正则获取内容
# gz = re.compile(r'<p class="duty duty-box">(.*?)</p>',re.S)
# zw = gz.findall(data2)
#
# print(zw)
#
#
# print('*' * 30)
# # print(url_list.findall(data))
# print(list1)
# print(list2)
# print(len(list1))
# print(res.url)
# print(res.headers)

def request_url(url,header,params=None):
    '''封装函数'''
    if params:
        res = requests.get(url,headers=header)
    else:
        res =requests.get(url,headers=header).text

    response = json.loads(res)

    return response

# for city in city_list:
#     city_json = json.dumps(city)
#     print(city_json)
# city_json = city_list[0]
num = 0
list1 = []
for i in range(0,39):
    # print(url2)
    url = url2 + str(i)
    header = User_Agt()
    data = request_url(url,header)
    if not data:
        print('页面异常')
        continue
    for q in range(20):

        try:
            dict = {'公司名称':data['data']['main']['data']['disp_data'][q]['officialname'],
                    '所属行业':data['data']['main']['data']['disp_data'][q]['industry'],
                    '岗位名称':data['data']['main']['data']['disp_data'][q]['title'],
                    '工资待遇':data['data']['main']['data']['disp_data'][q]['ori_salary'],
                    '岗位需求':data['data']['main']['data']['disp_data'][q]['description'],
                    '招聘网址':data['data']['main']['data']['disp_data'][q]['url'],
                    '发布时间':data['data']['main']['data']['disp_data'][q]['startdate'],
                    '结束时间':data['data']['main']['data']['disp_data'][q]['enddate']}
            # list2.append(':' + )
            # list2.append(':' + data['data']['main']['data']['disp_data'][q]['ori_salary'])
            # list2.append('岗位需求:'+ )
            # list2.append('招聘网址:' + data['data']['main']['data']['disp_data'][q]['url'])
        except Exception as e:
            print('数据异常 %s' % i)
            continue

        num +=1
        list1.append(dict)

    data1 = pandas.DataFrame(list1)
    data1.to_csv('xxx.csv',encoding='gb18030')
print(num)