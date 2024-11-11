import pandas as pd
import joblib

# 加载训练好的模型
model = joblib.load('../models/play_count_prediction_model_detail.pkl')

# 准备要预测的数据（示例数据）
new_data = pd.DataFrame({
    'favorite': [3500, 4800, 9200, 1500, 7000, 8400, 4300, 9100, 6200, 7800,
                  5100, 6100, 4500, 3900, 6600, 8600, 5500, 7300, 3200, 9700],
    'comments': [45, 110, 230, 90, 305, 180, 70, 250, 140, 200,
                 120, 300, 55, 85, 400, 260, 170, 215, 60, 350]
})

# 使用模型进行预测
predictions = model.predict(new_data)

# 输出预测结果
for i, pred in enumerate(predictions):
    print(f"示例数据 {i + 1} 的预测播放次数: {abs(int(pred))}")
