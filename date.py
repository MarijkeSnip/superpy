import datetime
import os.path
from datetime import date, datetime
import datetime
import pandas as pd

#date today
now = date.today()

#file
date_file = ("date.txt")

#return set date from file
def return_date():
    date=''
    with open(date_file,"r") as file:
        for line in file:
            date = pd.to_datetime(line, format='%Y-%m-%d').date()
            return date


#set date in date.txt file with set amount of days (a) from system date
def advance_days(days):

    current_date = return_date()
 
    set_date = current_date + datetime.timedelta(days)
    
    with open(date_file, "w") as file:
        file.write(str(set_date))
    print(f"Date is set to (yyyy-mm-dd): {set_date}")


#set date to entered date
def change_date(date):
        
    with open(date_file, "w") as file:
        file.write(str(date))
    print(f"Date is set to (yyyy-mm-dd): {date}")


#set date today
def set_today():
        
    with open(date_file, "w") as file:
        file.write(str(now))
    print(f"Date is set to (yyyy-mm-dd): {now}")


#print set date
def print_date():
    current_date = ''
    with open(date_file,"r") as file:
        for line in file:
            current_date = line
    print(f'Date is currently set to (yyyy-mm-dd): {current_date}')   



