import pandas as pd

# 读取数据并指定列名
music_list = pd.read_csv('../music_data/music_list.csv', header=None, names=['playlist_id', 'title', 'plays', 'creator'])
music_detail = pd.read_csv('../music_data/music_detail.csv', header=None, names=['title', 'type', 'introduce', 'plays', 'favorite', 'comments', 'songs'])

# 数据清洗 - 将播放次数、收藏数和评论数转换为数值格式
for col in ['plays', 'favorite', 'comments']:
    music_detail[col] = music_detail[col].replace({'万': '*10000'}, regex=True).replace({'收藏': '0'}, regex=True).map(pd.eval).astype(int)
music_list['plays'] = music_list['plays'].replace({'万': '*10000'}, regex=True).map(pd.eval).astype(int)

# 去除缺失值和重复值
music_list.dropna(inplace=True)
music_list.drop_duplicates(inplace=True)
music_detail.dropna(inplace=True)
music_detail.drop_duplicates(inplace=True)

# 保存清洗后的数据
music_list.to_csv('../music_data/cleaned_music_list.csv', index=False)
music_detail.to_csv('../music_data/cleaned_music_detail.csv', index=False)

print("数据清洗完成，结果已保存到 'cleaned_music_list.csv' 和 'cleaned_music_detail.csv'")
