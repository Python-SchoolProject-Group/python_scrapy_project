import redis

r = redis.Redis(host='localhost', port=6379, db=0)
for offset in range(0, 1715, 35):
    url = f'https://music.163.com/discover/playlist/?cat=华语&order=hot&limit=35&offset={offset}'
    r.lpush('test', url)
