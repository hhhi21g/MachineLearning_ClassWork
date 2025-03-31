import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# 读取合并后的数据
data = pd.read_csv("final_stock_sentiment_data.csv")

# 选择特征和目标变量
features = ['open', 'high', 'low', 'vol', 'sentiment_score', 'sentiment_3d_avg', 'sentiment_7d_avg']
X = data[features]
y = data['label']  # 1 涨，0 跌

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 训练 SVM 模型
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')  # 高斯核
svm_model.fit(X_train, y_train)

# 预测
y_pred = svm_model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"SVM 模型准确率: {accuracy:.4f}")

# 输出详细分类报告
print(classification_report(y_test, y_pred))
