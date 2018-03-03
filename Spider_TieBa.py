#coding=utf-8
import os
import re
import socket
import requests
import time
import urllib.request as request
from threading import Thread
import bs4
from multiprocessing import Process



class Reqt(object):

    # 初始化
    def __init__(self, url, headers=None, params=None, page_num=1):

        # socket 连接时间
        socket.timeout = 60
        self.url = [url+'pn={}'.format(nums*50) for nums in range(page_num)]
        self.headers = headers
        self.params = params
        self.page_num = page_num

    # 发送请求并获取网页内容
    def __send_url(self, num):

        response = requests.get(url=self.url[num],
                                params=self.params,
                                headers=self.headers)
        print('==========', response.url)
        response = response.content.decode('utf-8')




        return response

    # 多线程保存页面至本地
    def __thd_save(self, names, page_i):

        if page_i == 0:print('开始获取网页',end='')

        print('>'*page_i)
        if page_i == self.page_num -1 :print('获取完成，开始保存图片')

        # 获取并保存
        try:

            res_html = self.__send_url(page_i)

            page_names = names+'/'+'第%s页'%(page_i+1)

            if not page_names in os.listdir('./%s'%names):

                os.mkdir(page_names)

            for line in res_html.splitlines():

                res_url = re.search(r'(http:|https)(.*?)\.(jpg)\s?', line)
                if res_url:

                    try:
                        with open('%s/%s.jpg' % (page_names, time.time()), 'wb') as sf:

                            # print('-------', res_url.group())
                            pic_s = request.urlopen(res_url.group())
                            pic_s = pic_s.read()

                            sf.write(pic_s)
                            sf.close()
                    except Exception as error:

                        pass
                else:
                    continue

            print('---------------->第%s页保存完成' % page_i)
        except Exception as error:

            print('<+++++++++++++错误：%s>' % error)

    # 开始运行
    def run_html(self):

        names = self.params['kw']

        # 创建以贴吧名为文件名的文件夹
        if not names in os.listdir('./'):

            os.mkdir(names)

        # 线程列表
        thd_list = []

        # 读取指定页范围内的网页并为其开启相应数量的线程
        for page_i in range(self.page_num):

            thds = Thread(target=self.__thd_save, args=(names, page_i))
            thds.start()
            thd_list.append(thds)

        # 等待并关闭线程
        for thd_en in thd_list:

            thd_en.join()
        print('《《网页爬取完成》》')


if __name__ == '__main__':

    # 请求参数
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}
    url_temp = 'https://tieba.baidu.com/f?'
    params = {'kw':'python', 'ie':'utf-8'}  # pn=0

    # 创建实例对象并运行方法
    reqt = Reqt(url_temp,
                headers=headers,
                params=params,
                page_num= 3)
    '''
        page_num 总页码数
        headers 请示头
        params 发送参数  --- kw:贴吧名称 
                            ie:编码方式 
                            pn：不用写（单页数量）
    '''

    reqt.run_html()







































