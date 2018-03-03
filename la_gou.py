# -*- coding:utf-8 -*-
import requests
import re
from User_agent import User_Agt

# url_list = 'http://zhaopin.baidu.com/api/quanzhiasync?query=python&city_sug=%E5%8C%97%E4%BA%AC&detailmode=close&rn=20&pn=20'

# url= 'https://www.lagou.com/jobs/4070707.html'
kw = {'wd':'python','pn':20}

url = 'http://www.baidu.com/s?'
headers= User_Agt()
print(headers)
res_data = requests.get(url,params= kw,headers=headers)
data = res_data.content.decode()

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(res_data.text)

# 查看响应内容，response.content返回的字节流数据
print(data)

# 查看完整url地址
print(res_data.url)

# 查看响应头部字符编码
print(res_data.encoding)

# 查看响应码
print(res_data.status_code)


