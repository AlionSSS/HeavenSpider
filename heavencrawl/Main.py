# -*- encoding: utf-8 -*-

"""

 天堂图片网爬虫Main
 
 Author: ALion
 
 Date: 2017/9/1 8:49
"""

import threading
from heavencrawl import threadpool
import time
import json
from heavencrawl import HttpUtils, FileUtils
from heavencrawl.Constants import *
from heavencrawl.ImageSpider import parse_html


def start(arg):
    print('【' + threading.current_thread().name + ' -> start】')

    url = BASE_URL + SECOND_URL + str(arg) + '.html'
    html = HttpUtils.get_html(url)

    for each in parse_html(html):
        name = each['name']
        img_url = 'http:' + each['imgUrl']
        print(threading.current_thread().name + ' ->', name, img_url)
        # 下载图片、保存
        content = HttpUtils.get_bytes(img_url)
        path = DIR_NAME + '/' + each['imgDir'] + '/' + each['name'] + '.jpg'
        FileUtils.save_file(path, content)
        # 存储为json文本
        mutexLock.acquire()
        imageList.append(each)
        FileUtils.save_text(DIR_NAME + '/images.json', json.dumps(imageList, ensure_ascii=False))
        mutexLock.release()
        # 暂停一下，再爬
        time.sleep(SLEEP_TIME)

    print('【' + threading.current_thread().name + ' -> over】')


mutexLock = threading.Lock()
imageList = []

if __name__ == '__main__':
    pool = threadpool.ThreadPool(THREAD_COUNT)
    requests = threadpool.makeRequests(start, list(range(START_PAGE, END_PAGE + 1)))
    [pool.putRequest(req) for req in requests]
    pool.wait()

    print('---main over---')
