# -*- encoding: utf-8 -*-

"""
 天堂图片网html解析
 
 Author: ALion
 
 Date: 2017/8/31 15:54
"""

from bs4 import BeautifulSoup
from heavencrawl import HttpUtils
from heavencrawl.Constants import BASE_URL


def parse_html(html):
    """
    解析html源码

    :param html: html代码
    :return: info生成器
    """

    # 第一层网页
    soup1 = BeautifulSoup(html, 'lxml')
    dirList1 = soup1.select('div.left > ul.ali > li > div > a')
    for each in dirList1:
        print(' -> ', '开始下载【' + each['title'] + '】')
        # 第二层网页
        html2 = HttpUtils.get_html(BASE_URL + each['href'])
        soup2 = BeautifulSoup(html2, 'lxml')
        dirList2 = soup2.select('div.left > ul > li > div > a')
        for each2 in dirList2:
            # 第三层网页
            html3 = HttpUtils.get_html(BASE_URL + each2['href'])
            soup3 = BeautifulSoup(html3, 'lxml')
            imgList = soup3.select('div.box')
            for each3 in imgList:
                soup4 = BeautifulSoup(str(each3), 'lxml')
                name = soup4.select('div#al_tit > h1')
                imgUrl = soup4.select('img#imgis')
                if len(name) != 0 and len(imgUrl) != 0:
                    info = {
                        'imgDir': each['title'],
                        'name': name[0].string.replace(' ', ''),
                        'imgUrl': imgUrl[0]['src']
                    }
                    yield info
