# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from idlelib.iomenu import errors

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
        self.db = self.client['music_datas']
        self.collection = self.db['music_list']

    def process_item(self, item, spider):
        collection_name = getattr(spider, 'collection_name', 'default_collection')
        collection = self.db[collection_name]
        try:
            collection.insert_one(ItemAdapter(item).asdict())
            return item
        except errors.PyMongoError as e:
            spider.logger.error(f"插入数据到MongoDB失败： {e}")
            raise DropItem(f"不能出入数据：{e}")
