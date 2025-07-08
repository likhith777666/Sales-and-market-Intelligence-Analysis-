import pandas as pd
import glob

def load_data(folder):
    files=glob.glob(folder+"/*.csv")
    dfs=[pd.read_csv(f,low_memory=False) for f in files]
    return pd.concat(dfs,ignore_index=True)

def clean_transform(df):
    df.drop_duplicates(inplace=True)
    df['OrderDate']=pd.to_datetime(df['OrderDate'],errors='coerce')
    df['Quantity']=pd.to_numeric(df['Quantity'],errors='coerce').fillna(0)
    df['Price']=pd.to_numeric(df['Price'],errors='coerce').fillna(0)
    df['Sales']=df['Quantity']*df['Price']
    df['Month']=df['OrderDate'].dt.to_period('M')
    return df

    









if __name__=="__main__":
    raw=load_data(r"C:\Users\asus\Downloads\Sales and market intelligence automation")
    cleaned=clean_transform(raw)
    cleaned.to_csv(r"C:\Users\asus\Downloads\Sales and market intelligence automation\cleaned_ecomerce_data.csv",index=False)
    print(raw.head())


