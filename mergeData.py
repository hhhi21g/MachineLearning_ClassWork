import pandas as pd

stock_data = pd.read_csv("601318_trading_data.csv")
sentiment_data = pd.read_csv("sentiment.csv")

# 确保日期格式一致
stock_data['trade_date'] = pd.to_datetime(stock_data['trade_date'], format='%Y%m%d')
sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])

# 按日期合并股票数据和情感得分
merged_data = stock_data.merge(sentiment_data, left_on='trade_date', right_on='date', how='left')

# 处理缺失值（可能某些日期无新闻）
merged_data.fillna({'sentiment_score': 0}, inplace=True)

# 计算过去 n 天的平均情感得分（滑动窗口）
merged_data['sentiment_3d_avg'] = merged_data['sentiment_score'].rolling(window=3).mean()
merged_data['sentiment_7d_avg'] = merged_data['sentiment_score'].rolling(window=7).mean()

# 定义涨跌幅（label）
merged_data['price_change'] = merged_data['close'].pct_change()
merged_data['label'] = (merged_data['price_change'] > 0).astype(int)  # 1 表示涨，0 表示跌

# 删除无用列
merged_data.drop(columns=['date'], inplace=True)

# 保存最终数据集
merged_data.to_csv("final_stock_sentiment_data.csv", index=False, encoding="utf-8-sig")

print(merged_data.head())