import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 读取清洗后的数据
music_detail = pd.read_csv('../music_data/cleaned_music_detail.csv')

# 特征选择
X = music_detail[['favorite', 'comments']]  # 根据需要扩展更多特征
y = music_detail['plays']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 训练回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测和评估模型
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# 保存模型
joblib.dump(model, '../models/play_count_prediction_model_detail.pkl')
