import os.path
import csv
from datetime import datetime
import pandas as pd
from date import return_date

#code voor inkopen


#locatie file
wd = os.getcwd()
file_path = os.path.join(wd, "bought2.csv")#instructie geven om dir superpy aan te maken

df=pd.read_csv('bought2.csv')
latest_id = 0 #p=df['id'].max()

#als productname icm prijs, aankoopdatum en exp_date niet bestaat nieuwe aanmaken, anders aantallen verhogen.
#Voor buy date wordt de ingestelde systemdate gebruikt.
def register_buy(name, price, quantity, exp_date):
    
    new_id = latest_id + 1 #Haalt de nieuwe id op
    buy_date = return_date() #ingestelde datum wordt opgehaald
    #format_buy_date = datetime.strptime(buy_date, '%Y/%M/%D') #moet YYYY-MM-DD zijn
    #format_exp_date = datetime.strptime(exp_date)
    product = [new_id, name, buy_date, price,quantity, exp_date]
    
    #print(product)
    
    with open(file_path, "a", newline='') as file: #a= append
        writer = csv.writer(file)
        writer.writerow(product)



#test om te kijken of het is toegevoegd door de laatste line te printen
"""def show_last_product():
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
        last_line = lines[-1]
        print(last_line)"""


register_buy('Beyond meat sausage', 4.50, 3.0, 2023-7-25)
#show_last_product()
