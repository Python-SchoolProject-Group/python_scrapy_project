import redis
from pymongo import MongoClient


def push_initial_urls():
    # 连接到 Redis 和 MongoDB
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    client = MongoClient('localhost', 27017, username='root', password='123456')
    db = client['music_datas']
    collection = db['music_list']

    for record in collection.find({}, {"url": 1}):
        # 确保每个 URL 是完整的
        url = record['url']
        if not url.startswith("http"):
            url = "https://music.163.com" + url
        r.lpush("detail_url_queue", url)


if __name__ == "__main__":
    push_initial_urls()
