import os.path
import csv
from datetime import datetime
import pandas as pd
from date import return_date

#code voor inkopen

#locatie file
wd = os.getcwd()
file_bought = os.path.join(wd, "bought.csv")#instructie geven om dir superpy aan te maken
file_inventory = os.path.join(wd, "inventory.csv")

date = return_date()

df_bought=pd.read_csv('bought.csv')

#dataframe met alleen niet vervallen data
filt_not_expired = df_bought['expiration_date'] > date 
df_not_expired = df_bought[filt_not_expired]

#dataframe om laatste id op te halen
latest_id = p=df_bought['id'].max()

#print(df_not_expired)

#als productname icm prijs, aankoopdatum en exp_date niet bestaat nieuwe aanmaken, anders aantallen verhogen.
#Voor buy date wordt de ingestelde systemdate gebruikt.
def register_purchase(productname, price, exp_date):
    
    new_id = latest_id + 1 #Haalt de nieuwe id op 
    buy_date = return_date() #ingestelde datum wordt opgehaald
    quantity = 1
    name = " ".join(productname) #alleen gebruikt voor print functie
    
    product = [new_id, name, buy_date, price, quantity, exp_date]
    
    #add to bought.csv file
    with open(file_bought, "a", newline='') as file: #a= append
        writer = csv.writer(file)
        writer.writerow(product)
        print(f'{name} is added')
    
    #add to inventory.csv file
    with open(file_inventory, "a", newline='') as file: #a= append
        writer = csv.writer(file)
        writer.writerow(product)
        #print(f'{name} is added')

#ophalen bought_id uit df inventory


#test om te kijken of het is toegevoegd door de laatste line te printen
"""def show_last_product():
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
        last_line = lines[-1]
        print(last_line)"""


#register_purchase('Beyond meat sausage', 4.50, '2023-07-25')
#register_buy('Vegan chocolate', 9.50, 5.0, '2024-05-25')
#show_last_product()
#print(df_bought)