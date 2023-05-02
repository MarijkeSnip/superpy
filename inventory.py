import os.path
import pandas as pd
import datetime
import csv
from date import return_date

#locatie file
wd = os.getcwd()
file_path = os.path.join(wd, "bought.csv")#instructie geven om dir superpy aan te maken
now = datetime.date.today()
file_bought = ('bought.csv')
file_sell = ('sell.csv')
set_date = return_date()

df_bought = pd.read_csv('bought.csv') #dataframe
productname = 'test 1'
print(productname)
name = " ".join(productname)
print(name)
df2 = df_bought.loc[(df_bought['product_name'] == productname)]
#print(df2)

if df2.empty:
    print(f'Product {productname} not available, please check inventory!')
else:
    print(df2)

#print(set_date)

#dict van items in bought list
def bought_id():
    
    df_bought = pd.read_csv('bought.csv')
    bought_id = df_bought.loc[(df_bought['price']==3.50)]
    #filt_not_expired = df_bought['expiration_date'] > set_date 
    #df_not_expired = df_bought[filt_not_expired]

    print(bought_id)


"""" def sold_items():
    df_sell = pd.read_csv('sell.csv')
    #filt_sold = df_sell['sell_date'] > set_date 
    #df_not_sold = df_bought[filt_not_expired]
    return df_sell"""

#print(bought_items())
#print(sold_items())

"""def get_available_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date()
    for item in bought_items:
        if item["id"] not in sold_ids and item["expiration_date"] >= today:
            available_products.append(item)
    return available_products"""

