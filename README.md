# 天堂图片网爬虫

**注：爬取[天堂图片网](http://www.ivsky.com)上的图片的爬虫，仅供交流学习之用，请勿用于商业用途**

## 特性
1. 网络请求-数据解析-文件存储 三层结构
2. 多线程下载
3. 网络自动重试
4. 错误日志记录
5. Python3

## 你可能需要
- pip3 install requests
- pip3 install beautifulsoup4
- pip3 install threadpool
- pip3 install retrying

## 项目结构
![](http://i.imgur.com/ZtBXF6v.png)

## 代码说明
- Main.py -> 主程序入口，业务处理
- ImageSpider.py -> 爬虫html解析
- HttpUtils.py -> 网络请求工具
- FileUtils.py -> 文件保存工具
- LogUtils.py -> 日志工具
- Constants.py -> 常量设置

### 为防止服务器压力过大，爬虫爬取的为中小图，想要大图的请自行解析

## LICENSE
```
 Copyright 2017 ALion

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```
