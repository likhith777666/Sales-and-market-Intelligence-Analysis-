import pandas as pd
from pytrends.request import TrendReq

df=pd.read_csv(r"C:\Users\asus\Downloads\Sales and market intelligence automation\cleaned_ecomerce_data.csv")
top_categorey=df.groupby('Category')['Price'].sum().nlargest(3)

pytrends=TrendReq()
for cat in top_categorey.index:
    kw=pytrends.build_payload([cat],timeframe='today 12-m')
    data=pytrends.interest_over_time()
    print(cat,data[cat].idxmax())
