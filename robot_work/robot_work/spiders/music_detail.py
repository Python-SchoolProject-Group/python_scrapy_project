import redis
import scrapy
from itemadapter import ItemAdapter
from scrapy_redis.spiders import RedisSpider
from bs4 import BeautifulSoup
from ..items import MusicDetailItem
from pymongo import MongoClient


class MusicDetailSpider(RedisSpider):
    name = 'music_detail_spider'
    redis_key = 'detail_url_queue'  # 从 Redis 获取起始 URL
    collection_name = 'music_detail'

    def __init__(self, *args, **kwargs):
        super(MusicDetailSpider, self).__init__(*args, **kwargs)
        self.r = redis.StrictRedis(host='10.34.13.96', port=6379, db=0)

    def start_requests(self):
        while True:
            url = self.r.rpop(self.redis_key)
            url = url.decode('utf-8')
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取歌单标题
        title = response.meta.get('title', '无标题')

        # 获取标签
        tags = [tag.get_text() for tag in soup.select('.u-tag i')]
        tag = '-'.join(tags) if tags else '无'

        # 获取歌单介绍
        text_element = soup.select_one('#album-desc-more')
        text = text_element.get_text().replace('\n', '').replace(',', '，') if text_element else '无'

        # 获取收藏量
        collection_element = soup.select_one('#content-operation i')
        collection = collection_element.get_text().replace('(', '').replace(')', '') if collection_element else '无'

        # 获取播放量、歌曲数和评论数
        play = soup.select_one('.s-fc6').get_text() if soup.select_one('.s-fc6') else '无'
        songs = soup.select_one('#playlist-track-count').get_text() if soup.select_one('#playlist-track-count') else '无'
        comments = soup.select_one('#cnt_comment_count').get_text() if soup.select_one('#cnt_comment_count') else '无'

        # 创建并保存 MusicDetailItem 实例
        item = MusicDetailItem(
            title=title,
            tag=tag,
            description=text,
            collection=collection,
            play=play,
            songs=songs,
            comments=comments
        )
        yield item