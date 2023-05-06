import os.path
import csv
from datetime import datetime
import pandas as pd
from date import return_date

#file
file_bought = "bought.csv"

#set date
set_date = return_date()

#dataframe
df_bought = pd.read_csv('bought.csv') 

# Convert the date in dataframe to datetime64
df_bought['buy_date'] = pd.to_datetime(df_bought['buy_date'], format='%Y-%m-%d')
df_bought['expiration_date'] = pd.to_datetime(df_bought['expiration_date'], format='%Y-%m-%d')

#dataframe to return last bought_id
latest_id = p=df_bought['bought_id'].max()

#register purchases
def register_purchase(productname, price, exp_date):
    
    new_id = latest_id + 1  
    quantity = 1
    
    product = [new_id, productname, set_date, price, quantity, exp_date]
    
    #add product to bought.csv file
    with open(file_bought, "a", newline='') as file: #a= append, maakt file aan indien niet gevonden
        writer = csv.writer(file)
        writer.writerow(product)
        print(f'{productname} is added to bought items')
    