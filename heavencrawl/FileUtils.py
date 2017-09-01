# -*- encoding: utf-8 -*-

"""
 File 文件存储工具
 
 Author: ALion
 
 Date: 2017/8/31 18:26
"""
import os


def save_text(path, text):
    """
    文本存储

    :param path: 存储路径
    :param text: 文本内容
    :return: None
    """

    __check_path(path)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def save_file(path, content):
    """
    文件字节流存储

    :param path: 存储路径
    :param content: byte字节流
    :return: None
    """

    __check_path(path)

    with open(path, 'wb') as file:
        file.write(content)


def __check_path(path):
    file_name = path.split("/")[-1]
    dir_path = path.replace(file_name, '')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
