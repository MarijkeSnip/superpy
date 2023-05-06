import pandas as pd
#from date import return_date
from purchase import df_bought #, file_bought
from sales import df_sell #, file_sell
from date import now 

#calculates total profit between given dates    
def total_profit(date1, date2=now):

    bought_items = df_bought.query('buy_date >= @date1 & buy_date <= @date2')
    bought_price = bought_items['price'].sum()
    sold_items = df_sell.query('sell_date >= @date1 & sell_date <= @date2')
    sale_price = sold_items['sell_price'].sum()

    total = round((sale_price-bought_price),2)

    print(f'The profit from date {date1} till {date2} is {total}')

