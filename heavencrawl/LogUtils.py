# -*- encoding: utf-8 -*-

"""
 日志工具
 
 Author: ALion
 
 Date: 2017/9/1 2:29
"""

import time
import os


def log(path, text):
    """
    生成日志

    :param path: 存储路径
    :param text: 日志内容
    :return: None
    """

    file_name = path.split("/")[-1]
    dir_path = path.strip(file_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    localtime = time.asctime(time.localtime(time.time()))
    text = '\n' + localtime + ' ' + text

    with open(path, 'a', encoding='utf-8') as file:
        file.write(text)
