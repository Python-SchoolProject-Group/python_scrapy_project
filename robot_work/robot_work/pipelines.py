# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
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
        self.client = MongoClient('10.34.40.237', 27017, username='root', password='123456')
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
