# coding=utf-8
import time
import sys
from aip import AipSpeech

APP_ID = '10778987'
API_KEY = 'keAvAhcDfmFZmoW6BTYyZDWj'
SECRET_KEY = 'aPHU19MZSmt83l3rWQzh4vkITZtNhuDx'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def audio_transform(content):
    # 返回语音识别内容
    result = client.synthesis(content,
                              'zh',
                              1,
                              {
                                  'vol': 5,
                              })

    titles = str(time.time())
    print(titles)
    # 结果判断
    if not isinstance(result, dict):

        with open('./%s.mp3' % titles, 'wb') as rf:

            rf.write(result)

        return titles
    else:

        return 'wrong'


if __name__ == '__main__':

    result = sys.argv[1]

    audio_transform(result)

