import pandas as pd
from date import return_date
import csv
from purchase import df_bought
from inventory import create_inventory_df

#file
file_sell = "sell.csv"

#set date by user
sell_date = return_date() 

#Dataframe
df_sell = pd.read_csv('sell.csv')
df_inventory = create_inventory_df(sell_date) #created from bought and sold items

# Convert the date in dataframe to datetime64
df_sell['sell_date'] = pd.to_datetime(df_sell['sell_date'], format='%Y-%m-%d')

#if sell.csv is empty it returns 1, otherwise last id + 1
def new_id():
    current_id = df_sell['sell_id'].max()
    if pd.isna(current_id) == True:
        current_id = 1
    else:
        current_id += 1
    return current_id



def sell_product(productname, price):

    sell_id = new_id() 
        
    #finds bought_id in inventory df
    try:
        filt_bought_id_name = (df_inventory['product_name'] == productname) 
        df_filtered = df_inventory.loc[filt_bought_id_name, ['bought_id', 'expiration_date']] 
        df_sorted = df_filtered.sort_values(by=['expiration_date']) #sort by expiration date
        bought_id = df_sorted.iloc[0]['bought_id'] #finds first row, this is the one with the nearest expiration date

        product = [sell_id, bought_id, productname, sell_date, price]
    
    #if bought_id is not available the product is not in stock on set date
    except:
        print(f'{productname} is not available on {sell_date}, please check inventory')
    
    #If product is available it is added to sell.csv
    else:
        with open(file_sell, "a", newline='') as file:
            csv_writer = csv.writer(file)    
            csv_writer.writerow(product)
            print(f'{productname} is added to sold items.')
       

