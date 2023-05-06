import os.path
import pandas as pd
#from datetime import date, datetime
from inventory import df_sell, now
from purchase import df_bought


#files
file_bought = ('bought.csv')
file_sell = ('sell.csv')


#shows revenue between given dates, default date2 = today
def total_revenue(date1, date2=now):

    sold_on_date = df_sell.query('sell_date >= @date1 & sell_date <= @date2')
    total_date = sold_on_date['sell_price'].sum()    

    print(f'The total revenue from {date1} till {date2} is {total_date}')

#shows revenue per month between given dates, default date2 = today
def total_revenue_per_month(date1, date2=now):

    df = df_sell.loc[:,['sell_date','sell_price']] #df with only date and price
    df_month_price = df.query('sell_date >= @date1 & sell_date <= @date2')
    df_sell_month = df_month_price.groupby(pd.Grouper(key='sell_date', freq='1M')).sum() #df where the sum of sell_price is grouped by month
    df_sell_month.index = df_sell_month.index.strftime('%Y-%m') #changes date format

    return df_sell_month


