import requests
from bs4 import BeautifulSoup


def parse1111(response):
    """解析歌单索引页"""
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取包含歌单详情页网址的标签
    ids = soup.select('.dec a')
    # 获取包含歌单索引页信息的标签
    lis = soup.select('#m-pl-container li')
    print(len(lis))
    for j in range(len(lis)):
        url = ids[j]['href']
        # 获取歌单标题,替换英文分割符
        title = ids[j]['title'].replace(',', '，')
        # 获取歌单播放量
        play = lis[j].select('.nb')[0].get_text()
        # 获取歌单贡献者名字
        user = lis[j].select('p')[1].select('a')[0].get_text()
        item = {
            'url': url,
            'title': title,
            'play': play,
            'user': user
        }
        print(item)



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}


if __name__ == '__main__':
    for offset in range(0,175,35):
        response = requests.get(f'https://music.163.com/discover/playlist/?order=hot&cat=欧美&limit=35&offset={offset}',headers=headers)
        parse1111(response=response)

