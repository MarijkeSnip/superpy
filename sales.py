import pandas as pd
from date import return_date
import csv

#from date import get_date
#from inventory import get_available_product
#from rich import print

file_sell = "sell.csv"
file_inventory = "inventory.csv" 

df_sell = pd.read_csv('sell.csv')
df_inventory = pd.read_csv('inventory.csv')
df_bought = pd.read_csv('bought.csv')

#print(df_bought)


#als sales id nog leeg is wordt id 1, anders max id + 1
def new_id():
    current_id = df_sell['sell_id'].max()
    if pd.isna(current_id) == True:
        current_id = 1
    else:
        current_id += 1
    return current_id

#functie om de naam te verwerken met spaties
"""def productname(product_name):
    name = " ".join(product_name)
    return name"""

#registreren sale. Moet eigenlijk kijken naar inventory en melding geven als product niet meer op voorraad is.
#Nog toevoegen: als file nog niet bestaat create sell aanmaken
def sell_product(productname, price):

    sell_id = new_id() 
    #name = " ".join(productname)
    sell_date = return_date()

    #print(productname)
    
    #ophalen bought_id uit df inventory
    filt_bought_id_name = (df_bought['product_name'] == productname) #probleem met de naam, werkt niet als ik variabele name gebruik
    df_filtered = df_bought.loc[filt_bought_id_name, ['id', 'expiration_date']] #haalt gefilterde naam en exp date op
    df_sorted = df_filtered.sort_values(by=['expiration_date']) #sorteren op exp date
    bought_id = df_sorted.iloc[0]['id'] #haalt de eerste id op
    
    print(filt_bought_id_name)
    print(df_filtered)
    print(df_sorted)
    print(bought_id)
    #print(type(productname))
    
    #haalt op uit een list
    #available_products = get_available_product(product_name)
    #bought_id = available_products[i]["id"]

    #print(df_sorted)

    product = [sell_id, bought_id, productname, sell_date, price]
    
    """with open(file_sell, "a", newline='') as file:
        csv_writer = csv.writer(file)    
        csv_writer.writerow(product)
        print(f'{name} is sold.')"""
        

sell_product('cookies', 1.25)