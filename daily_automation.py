import pandas as pd
from datetime import datetime, timedelta
from Collect_data import load_data, clean_transform

def recent_data(df, days=30):
    cutoff=datetime.now()-timedelta(days=days)
    return df[df['OrderDate']>=cutoff]





if __name__=="__main__":
    df=clean_transform(load_data(r"C:\Users\asus\Downloads\Sales and market intelligence automation"))
    last_month=recent_data(df)
    #last_month.to_excel(r"C:\Users\asus\Downloads\Sales and market intelligence automation\Thirtydays_report.xlsx", index=False)
