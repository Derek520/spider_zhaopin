# -*- coding:utf-8 -*-
import requests,re,os
from User_agent import User_Agt
from time import time
import threading,multiprocessing
from threading import current_thread
# <img src="https//pic.qiushibaike.com/system/pictures/12006/120063201/medium/app120063201.jpg" alt="糗事#120063201" class="illustration" width="100%" height="auto">


# https://pic.qiushibaike.com/system/pictures/2006/120063201/medium/app120063201.jpg

class XiuShiBaiKe(object):
    '''糗事百科'''

    def __init__(self):

        self.url = 'https://www.qiushibaike.com/imgrank/page/{}/'
        self.user_agt = User_Agt()

    def get_url(self,page):
        '''请求访问'''
        data = requests.get(self.url.format(page),headers=self.user_agt)
        str_data = data.content.decode()
        # return str_data
        threading.Thread(target=self.save_image,args=(str_data,)).start()
        # self.save_image(str_data)
        # pro = multiprocessing.Process(target=self.save_image, args=(str_data,))
        # pro.start()
        # # pro.join()

    def get_image_url(self,file_path,image):
        '''多线程图片'''


        with open(file_path, 'wb') as f:
            f.write(image.content)

    def save_image(self,str_data):
        '''保存数据'''
        contentpat = 'target="_blank">\s<img src="//(.*?)" alt=?'
        image_list = re.compile(contentpat).findall(str_data)

        # print(image_list)
        # print(len(image_list))

        for image in image_list:
            if image_list.index(image)<=24:
                url = 'https://'+ image
                data = url.split('/')[-1]
                print(url)
                thred = threading.current_thread()
                print(thred)
                image = requests.post(url, headers=self.user_agt)

                file_path = os.path.join('xsbk', '{}.jpg'.format(data))

                thred = threading.Thread(target=self.get_image_url,args=(file_path,image))
                thred.getName()
                thred.start()
                thred.join()


                # pro = multiprocessing.Process(target=self.get_image_url,args=(url,data))
                # print(pro.name)
                # pro.start()
                # pro.join()
                # image = requests.post(url,headers = self.user_agt)
                # image = self.get_image_url(url)
                # print(image)
                # file_path = os.path.join('xsbk','{}.jpg'.format(data))
                #
                # with open(file_path,'wb') as f:
                #     f.write(image.content)



    def run(self):
        '''逻辑'''
        # 1.请求访问
        # 遍历访问
        start = time()
        for i in range(1,3):
            # pro = multiprocessing.Process(target=self.get_image_url,args=(url,data))
            # print(pro.name)
            # pro.start()
            # pro.join()
            self.get_url(i)
            # self.save_image(str_data,i)
        end =time()
        print(end-start)

if __name__ == '__main__':
    xs = XiuShiBaiKe()

    xs.run()


