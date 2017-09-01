# -*- encoding: utf-8 -*-

"""
 Http 网络请求工具
 
 Author: ALion
 
 Date: 2017/8/31 18:19
"""

import requests
import random
from retrying import retry
from heavencrawl import LogUtils
from heavencrawl.Constants import *


@retry(wait_fixed=3000, stop_max_attempt_number=9)
def get_html(url):
    """
    获取Html源码

    :param url: 链接地址
    :return: html源码
    """
    try:
        response = requests.get(url, headers=__gen_headers())
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        else:
            print("网络访问出错，非200")
    except:
        LogUtils.log('./error.log', url)
        raise Exception('网络异常')


@retry(wait_fixed=3000, stop_max_attempt_number=9)
def get_bytes(url):
    """
    获取File字节流

    :param url: File地址
    :return: response.content
    """

    try:
        response = requests.get(url, headers=__gen_headers())
        if response.status_code == 200:
            return response.content
        else:
            print("网络访问出错，非200")
    except:
        LogUtils.log('./error.log', url)
        raise Exception('网络异常')


def __gen_headers():
    headers = {
        "User-Agent": USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)],
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    return headers
