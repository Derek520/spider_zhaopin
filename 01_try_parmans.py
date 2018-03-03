# -*- coding:utf-8 -*-
import requests
from User_agent import User_Agt
from multiprocessing import Process
from multiprocessing import Pool
from threading import Thread

headers=User_Agt()


# URL编码
temp = '李毅'

url = 'https://tieba.baidu.com/f?kw='+ temp +'&pn={}'

# def parmsns(url):
#
#     response = requests.get(url,headers=headers)
#
#     return response
#
# num=1
# for i in range(0,5000,50):
#
#     data = url.format('李毅',i)
#     res = parmsns(data)
#     with open('%s.html'%num,'wb') as f:
#         f.write(res.content)
#     num+=1
# if __name__ == '__main__':
#     '''
#     for i in range(10):
#         main(i*10)
#     '''
#     pool = Pool() #建立进程池
#     pool.map(main, (i*10 for i in range(10)))#映射到主函数中进行循环

# 列表推导式

def pa_chong(url):

        data = requests.get(url,headers=headers)

        # 保存路径
        file_path = "{}-第{}页.html".format(temp,url_list.index(url)+1)
        with open(file_path,'wb') as f:
            f.write(data.content)

if __name__ == '__main__':
    url_list = [url.format(i * 50) for i in range(1000)]
    for url in url_list:
        pa_chong(url)

