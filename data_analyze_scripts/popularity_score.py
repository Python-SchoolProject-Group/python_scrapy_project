import pandas as pd

# 参数设定
alpha = 0.5  # 播放次数权重
beta = 0.3   # 收藏数权重
gamma = 0.2  # 评论数权重

# 读取清洗后的数据
music_detail = pd.read_csv('../music_data/cleaned_music_detail.csv')

# 计算流行度评分
music_detail['popularity_score'] = (alpha * music_detail['plays'] +
                                    beta * music_detail['favorite'] +
                                    gamma * music_detail['comments'])

# 排序并保存
music_detail.sort_values('popularity_score', ascending=False, inplace=True)
music_detail.to_csv('../music_data/popularity_ranking_detail.csv', index=False)

print("流行度评分计算完成，结果已保存到 'popularity_ranking_detail.csv'")
