#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


ECUKdf=pd.read_csv("C:/Users/asus/Downloads/Market & Sales Intelligence Automation project/ecommerce_data_uk.csv",encoding='ISO-8859-1')
Eledf=pd.read_csv("C:/Users/asus/Downloads/Market & Sales Intelligence Automation project/electronics_sales.csv")

ECUKdf.rename(columns={
    'InvoiceNo':'OrderNo',
    'Description':'Product',
    'UnitPrice':'Price',
    'Country':'Region',
    'InvoiceDate':'OrderDate'
},inplace=True)

Eledf.rename(columns={
    'Order Date':'OrderDate',
    'Quantity Ordered':'Quantity',
    'Price Each':'Price'
    
},inplace=True)





# In[3]:


Eledf.head(10)


# In[4]:


ECUKdf.head(10)


# In[ ]:





# In[5]:



def extract_category(product):
    if 'shirt' in product.lower() or 'jeans' in product.lower():
        return 'Fashion'
    elif 'USB' in product.lower() or 'laptop' in product.lower():
        return 'Electronics'
    else:
        return 'General'

ECUKdf['Category']=ECUKdf['Product'].fillna('').apply(extract_category)

ECUKdf['CustomerType'] ='Retail'

Eledf['CustomerType']='Retail'


# In[6]:



def extract_region(address):
    if pd.isna(address):
        return 'Unknown'
    try:
        parts=address.split(',')
        if len(parts)>=3:
            state_zip=parts[2].strip()
            state=state_zip.split()[0]
            return state
        elif len(parts)==2:
            return parts[1].strip()
        else:
            return 'Unknown'
    except:
        return 'Unknown'
        
            
            
    

Eledf['Region']=Eledf['Purchase Address'].apply(extract_region)


# In[7]:


def extract_category_Eledf(product):
    if pd.isna(product):
        return 'General'
    
    product=product.lower()
    
    electronics_keywords=['usb', 'laptop', 'charger', 'monitor', 'phone', 'cable', 'adapter', 'keyboard', 'mouse']
        
    if any(k in product for k in electronics_keywords):
        return 'Electronics'
    else:
        return 'General'



Eledf['Category']=Eledf['Product'].apply(extract_category_Eledf)


# In[8]:


Eledf.head(10)


# In[9]:


ECUKdf.fillna({'Product':'Unknown','Region':'Unknown'},inplace=True)
Eledf.fillna({'Product':'Unknown','Region':'Unknown'},inplace=True)


# In[10]:


ECUKdf.head(10)


# In[11]:


ECUKdf=ECUKdf[['OrderDate','Product','Category','Quantity','Price','Region','CustomerType']]
Eledf=Eledf[['OrderDate','Product','Category','Quantity','Price','Region','CustomerType']]


combined=pd.concat([ECUKdf,Eledf],ignore_index=True)

combined.head(20)


# In[12]:


combined.tail(20)


# In[14]:


combined.to_csv('C:/Users/asus/Downloads/ecomerce_combined_dataSet.csv',index=False)


# In[ ]:




