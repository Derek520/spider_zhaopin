# -*- coding:utf-8 -*-
import requests
from User_agent import User_Agt
user_url = 'http://www.renren.com/327550029/profile'
post_url='http://www.renren.com/PLogin.do'
post_data ={"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers=User_Agt()

# 实例化session
session=requests.session()

res = session.post(post_url,data=post_data,headers=headers)

# 请求个人主页
session.get(user_url,headers=headers)

res2 =session.post(user_url,data=post_data,headers=headers)

print(res2.status_code)