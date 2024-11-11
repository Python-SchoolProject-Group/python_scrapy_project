import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取清洗后的数据
music_detail = pd.read_csv('../music_data/cleaned_music_detail.csv')

# 绘制播放次数、收藏数和评论数的分布图
plt.figure(figsize=(14, 7))
sns.histplot(music_detail['plays'], bins=30, kde=True, color='blue', label='Plays')
sns.histplot(music_detail['favorite'], bins=30, kde=True, color='green', label='Favorites')
sns.histplot(music_detail['comments'], bins=30, kde=True, color='red', label='Comments')
plt.title('播放次数、收藏数和评论数分布')
plt.xlabel('数量')
plt.ylabel('频数')
plt.legend()
plt.show()
