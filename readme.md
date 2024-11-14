# 基于Scrapy-Redis的网易云音乐歌单爬虫和数据分析

本代码的解析部分来自天津科技大学的一位开源仁兄，在这里特别感谢这位大佬分享代码，感谢感谢！！

## 以下是原文：

https://github.com/MYXHcode/Python-data-analysis-preliminary-project-data-visualization-music-list-analysis-system-TUST-2022

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

# Python 基于Scrapy-redis框架对网易云音乐歌单的分布式爬虫系统及数据可视化 大学编程作业（GUET 桂林电子科技大学 2024年）

## 一、项目简介

基于Scrapy-redis框架对网易云音乐歌单的分布式爬虫系统及数据可视化 ，我使用了 Python 丰富的第三方开源模块，如 scrapy-redis,numpy, pandas, matplotlib, time, requests, squarify, jieba, wordcloud, bs4 等来制作，实现了对网易云音乐歌单数据的获取，对歌单数据进行可视化分析，得出歌单的评论、收藏、播放、贡献、分布的数量图，并提出歌单优化的建议。通过这次 Python 数据分析初探项目的实践，我巩固了 Python 的语法知识，熟练应用了各个第三方开源模块，为之后的 Python 数据分析学习打下基础。

这个项目是我大二的python大作业，分享出来一方面希望可以帮助初学者，另一方面希望能让同学们可以从目前大学中普遍毫无价值的形式主义作业中解脱出来，别被这些无聊的东西浪费自己宝贵的时间，更加高效地学习优质计算机知识和主流编程技术，一起发扬开源精神，感受互联网技术的美好愿景。

## 二、交流学习

互联网开源精神需要大家一起互相交流学习，互相支持奉献。欢迎大家与我友好交流。

加我 QQ：643733581 可对各种问题进行友好交流与讨论，感谢大家的支持！

## 三、项目模块

#### 1. 环境准备：

先把**requirement.txt**的依赖安装完成，再确保你的电脑能运行docker。之后运行docker-compose来启动redis和MongoDB的镜像服务。

#### 2. 数据爬取，爬虫模块：

使用**list_url_queue**来进行分布式爬虫的搭建，首先需要爬取你想要的榜单基本信息，先通过start_requests把所需爬取的url推入redis的**list_url_queue**队列中，再通过循环将url全部放入requests队列，代码如下所示：

```python
def start_requests(self):
    """生成带有不同 offset 的 URL 并推送到 Redis"""
    for offset in range(0, 1715, 35):  # 从 0 到 2000，步长为 35
        url = f'https://music.163.com/discover/playlist/?cat=华语&order=hot&limit=35&offset={offset}'
        self.r.lpush(self.redis_key, url)  # 将生成的 URL 推送到 Redis
    while True:
        url = self.r.rpop(self.redis_key)
        url = url.decode('utf-8')
        yield scrapy.Request(url=url, callback=self.parse)
```

再通过解析函数来解析出数据，其中包括了对每个榜单的详细信息介绍的url，把这些url放入**detail_url_queue**队列，然后构建item并将其传入pipline，然后**music_list_spider**就可以开始爬取获取到的每个榜单的详细信息了。**music_list_spider**从redis的**detail_url_queue**中取出url进行解析构造item然后传入pipline进行保存。

#### 3. 数据存储

在pipline中连接到MongoDB数据库，然后将spider传入的item进行插入。代码如下：

```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from pymongo import errors
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.exceptions import DropItem


class RobotWorkPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline:
    def __init__(self):
        # 连接到 MongoDB
        self.client = MongoClient('localhost', 27017, username='root', password='123456')
        pymongo_logger = logging.getLogger('pymongo')
        pymongo_logger.setLevel(logging.ERROR)
        self.db = self.client['music_datas']

    def process_item(self, item, spider):
        collection_name = ''
        if spider.name == 'music_list_spider':
            collection_name = 'music_list'
        elif spider.name == 'music_detail_spider':
            collection_name = 'music_detail'
        else:
            spider.name = 'default'
        collection = self.db[collection_name]
        try:
            collection.insert_one(ItemAdapter(item).asdict())
            return item
        except errors.PyMongoError as e:
            spider.logger.error(f"Failed to insert item into MongoDB: {e}")
            raise DropItem(f"Cannot insert item: {e}")
```



#### 4. 数据可视化

使用各种图表对爬取到的数据进行可视化处理，是数据看起来更加直观。效果如下：

![image-20241114150306207](https://cdn.jsdelivr.net/gh/1zhangluo1/images/images/image-20241114150306207.png)

![image-20241114150315189](https://cdn.jsdelivr.net/gh/1zhangluo1/images/images/image-20241114150315189.png)

![image-20241114150330942](https://cdn.jsdelivr.net/gh/1zhangluo1/images/images/image-20241114150330942.png)

![image-20241114150340369](https://cdn.jsdelivr.net/gh/1zhangluo1/images/images/image-20241114150340369.png)



#### 5. 对爬取到的数据进行数据分析

详细代码在**data_analyze_scripts**文件夹中

#### 6. 对项目进行docker打包

在**docker**文件夹下的Dockerfile中有对于项目打包的配置文件

#### 7. 补充说明

如有对于此项目有疑问或者想进一步了解的可联系作者**QQ: 643733581**并备注来意。