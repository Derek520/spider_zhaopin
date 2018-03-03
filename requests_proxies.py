# -*- coding:utf-8 -*-
# import requests
#
# # 根据协议类型，选择不同的代理
# proxies = {"http": "http://139.129.166.68:3128"}
#
# response = requests.get("http://www.baidu.com", proxies = proxies)
# print response.text


# 私密代理
import requests

# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = { "http": "mr_mao_hacker:sffqry9r@61.188.191.27:80"}

response = requests.get("http://www.baidu.com", proxies = proxy)

