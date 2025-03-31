import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 读取合并后的数据
data = pd.read_csv("final_stock_sentiment_data.csv")

# 选择特征和目标变量
features = ['open', 'high', 'low', 'vol', 'sentiment_score', 'sentiment_3d_avg', 'sentiment_7d_avg']
X = data[features]
y = data['label']  # 1 涨，0 跌

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练决策树模型
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估模型
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.4f}")

import matplotlib.pyplot as plt

feature_importance = model.feature_importances_
plt.barh(features, feature_importance)
plt.xlabel("Feature Importance")
plt.ylabel("Feature Name")
plt.title("决策树特征重要性分析")
plt.show()
