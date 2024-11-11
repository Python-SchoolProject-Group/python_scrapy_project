import pandas as pd

# 读取聚类和流行度评分数据
music_detail = pd.read_csv('../music_data/clustered_music_detail.csv')

# 计算每个聚类的平均播放次数、收藏数和评论数
cluster_analysis = music_detail.groupby('Cluster')[['plays', 'favorite', 'comments']].mean().sort_values(by='plays', ascending=False)

# 输出分析结果
print("聚类分析结果：")
print(cluster_analysis)

# 生成内容创作建议
top_cluster = cluster_analysis.index[0]
print(f"\n内容创作建议：聚焦于第 {top_cluster} 类中的歌曲特征，如高播放次数、高收藏数和高评论数，以吸引更多用户。")
