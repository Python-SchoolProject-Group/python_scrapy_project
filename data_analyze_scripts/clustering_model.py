import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 读取清洗后的详细数据
music_detail = pd.read_csv('../music_data/cleaned_music_detail.csv')

# 选择用于聚类的特征
X = music_detail[['plays', 'favorite', 'comments']]

# 使用 Elbow Method 确定最佳聚类数
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# 绘制肘部图
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# 使用最佳 k 值进行聚类（假设 k=3）
kmeans = KMeans(n_clusters=3, random_state=42)
music_detail['Cluster'] = kmeans.fit_predict(X)

# 保存聚类结果
music_detail.to_csv('../music_data/clustered_music_detail.csv', index=False)

print("聚类模型训练完成，结果已保存到 'clustered_music_detail.csv'")
