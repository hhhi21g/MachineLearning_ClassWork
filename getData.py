import pandas as pd
import tushare as ts
from snownlp import SnowNLP

# 设置 token（需要申请 Tushare 账号）
ts.set_token("75bd31aac4f8b7dadd9a33820ea44a0b032b935adcfee546c9415172")
# ts.set_token("5f0b6cb4ec8f84b45401667cdb8501ff6f04d72fdc587a679e007f69")
# ts.set_token("0434d4ef9684308ad27f9f73335da3d19ca644604b728a3996a8e6ef")
# ts.set_token("196c08767c4f01c1241e774499a515946014da9fad847abd8858ad23")
# ts.set_token("50bdc673991399d9ea22003c2763ac35c13fba355e47bc6b1a735aac")
# ts.set_token("31cdeffa4aa62446d10b5cb0c7e9a6e7165870a10033a95f30bb03b5")
# ts.set_token("91207c40f8a15ced3c75eb3b9bf985c9aaa6356dbd1293fd08085a62")
pro = ts.pro_api()

# 获取 601318 最近的交易数据(中国平安)
df = pro.daily(ts_code='601318.SH', start_date='20240329', end_date='20250329')

# news1 = pro.news(src='sina', start_date='20240329', end_date='20250329')  # 新浪财经
# news2 = pro.news(src='10jqka', start_date='20240329', end_date='20250329')  # 同花顺
news3 = pro.news(src='eastmoney', start_date='20240329', end_date='20250329')  # 东方财富

# cctv_news = pro.cctv_news(start_date = '20240329',end_date = '20250329')
# filt_cctv = cctv_news[cctv_news['content'].str.contains(r"中国平安|平安|601318", na=False, regex=True)]
# print(filt_cctv.head())
# filt_cctv.to_csv("cctv_pingan_news.csv",index=False,encoding="utf-8-sig")
news = pd.concat([news3],ignore_index=True)
news_filt = news[news['title'].str.contains(r"中国平安||平安||601318",na=False)]
print(news_filt.head())

# 保存到 CSV
df.to_csv("601318_trading_data.csv", index=False, encoding="utf-8-sig")
# 只保留新闻标题
news_filt[['title']].to_csv("china_pingan_news.csv", index=False, encoding="utf-8-sig")

sen = pd.read_csv("china_pingan_news.csv")
sen["sentiment_score"] = sen["title"].apply(lambda x:SnowNLP(str(x)).sentiments)
sen.to_csv("sentiment.csv",index=False,encoding="utf-8-sig")
