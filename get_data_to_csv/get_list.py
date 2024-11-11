import csv
from pymongo import MongoClient

# MongoDB 连接配置
mongo_client = MongoClient('jzhangluo.com', 27017, username='root', password='123456')
db = mongo_client['music_datas']
collection = db['music_list']

# 导出 MongoDB 数据为 CSV 文件
def export_mongodb_to_csv():
    music_items = collection.find()
    with open('../music_data/chinese_music_list.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['url', 'title', 'play', 'user'])  # 表头
        for item in music_items:
            writer.writerow([item.get('url', ''), item.get('title', ''), item.get('play', ''), item.get('user', '')])
    print("数据已导出至 exported_music_list.csv")

export_mongodb_to_csv()
