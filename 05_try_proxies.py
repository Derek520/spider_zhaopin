# -*- coding:utf-8 -*-
import requests

proxies = {'http':'http://46.242.38.142:8081'}

url = 'http://www.baidu.com'

resp = requests.get(url,proxies=proxies)

print(resp.status_code)