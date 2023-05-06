import pandas as pd
from date import now
from purchase import df_bought 
from tabulate import tabulate


#Dataframes
df_sell = pd.read_csv("sell.csv") 

# Convert the date to datetime64
df_sell['sell_date'] = pd.to_datetime(df_sell['sell_date'], format='%Y-%m-%d')

#create df for sales
def create_inventory_df(date=now):
    
    #dataframes filtered on date, default vandaag
    available_bought = df_bought.query('buy_date <= @date')
    sold_items = df_sell.query('sell_date <= @date')

    #inventory filter checks if sold items are not in available bought
    filt_inventory = ~available_bought.bought_id.isin(sold_items.bought_id)
    df_inventory = available_bought.loc[filt_inventory]

    return df_inventory


def show_inventory(date=now):
    
    df_inventory= create_inventory_df(date)
    
    if df_inventory.empty:
        print(f'There is no inventory on {date}')
    else:
        print(f'Inventory on {date}')
        print(tabulate(df_inventory, headers = 'keys', tablefmt='pretty'))

def export_inventory(format, date=now):
    
    df_inventory = create_inventory_df(date)
    
    if format == "c":
        with open('inventory_csv', "w", newline="") as file:
            df_inventory.to_csv('inventory.csv', index=False)
            print(f"CSV file with inventory on {date} is created")

    if format == "x":
        df_inventory.to_excel('inventory.xlsx') 
        print(f"xls file with inventory on {date} is created")
