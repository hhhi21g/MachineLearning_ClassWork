import tushare as ts

# 设置 token（需要申请 Tushare 账号）
ts.set_token("fcdf7da144d22a545a8ed5e4ad98a4be5f489c75a8ae7a396b3452b1")
pro = ts.pro_api()

# 获取 601318 最近的交易数据(中国平安)
df = pro.daily(ts_code='601318.SH', start_date='20240329', end_date='20250329')

news = pro.news(src='sina',start_date='20240329', end_date='20250329')
news_filt = news[news['title'].str.contains("中国平安",na=False)]
print(news_filt.head())
# 保存到 CSV
df.to_csv("601318_trading_data.csv", index=False, encoding="utf-8-sig")
