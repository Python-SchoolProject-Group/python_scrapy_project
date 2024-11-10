import scrapy
from scrapy_redis.spiders import RedisSpider
from bs4 import BeautifulSoup
import redis
from ..items import MusicListItem


class MusicListSpider(RedisSpider):
    name = 'music_list_spider'
    redis_key = 'list_url_queue'  # 从 Redis 获取起始 URL

    def __init__(self, *args, **kwargs):
        super(MusicListSpider, self).__init__(*args, **kwargs)
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def start_requests(self):
        """生成带有不同 offset 的 URL 并推送到 Redis"""
        for offset in range(0, 1715, 35):  # 从 0 到 2000，步长为 35
            url = f'https://music.163.com/discover/playlist/?cat=华语&order=hot&limit=35&offset={offset}'
            self.r.lpush(self.redis_key, url)  # 将生成的 URL 推送到 Redis
        while True:
            url = self.r.rpop(self.redis_key)
            url = url.decode('utf-8')
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """解析歌单索引页"""
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取包含歌单详情页网址的标签
        ids = soup.select('.dec a')
        # 获取包含歌单索引页信息的标签
        lis = soup.select('#m-pl-container li')

        for j in range(len(lis)):
            url = ids[j]['href']
            # 获取歌单标题,替换英文分割符
            title = ids[j]['title'].replace(',', '，')
            # 获取歌单播放量
            play = lis[j].select('.nb')[0].get_text()
            # 获取歌单贡献者名字
            user = lis[j].select('p')[1].select('a')[0].get_text()
            # 创建并保存 MusicListItem 实例
            item = MusicListItem(url=url, title=title, play=play, user=user)
            # 将详情页 URL 推送到 Redis 队列 detail_url_queue
            self.r.lpush('detail_url_queue', f"https://music.163.com{url}")
            yield item
