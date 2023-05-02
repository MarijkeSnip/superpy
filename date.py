import datetime
import os.path

"""Your program should have an internal conception of what day it is -- perhaps saved to a simple text file 
-- that we can advance time by two days by using a command like:
$ python super.py --advance-time 2"""

#locatie date.txt file
wd = os.getcwd()
file_path = os.path.join(wd, "date.txt")#instructie geven om dir superpy aan te maken

#set date in date.txt file with set amount of days
def change_date(days):
    
    #file_name = 'date.txt'
    today = datetime.date.today()
    set_date = today + datetime.timedelta(days)
    
    with open(file_path, "w") as file:
        file.write(str(set_date))
    print(f"Date is set to (yyyy-mm-dd): {set_date}")

def set_today():
    
    today = datetime.date.today()
    
    with open(file_path, "w") as file:
        file.write(str(today))
    print(f"Date is set to (yyyy-mm-dd): {today}")

def print_date():
    current_date = ''
    with open(file_path,"r") as file:
        for line in file:
            current_date = line
    print(f'Date is currently set to (yyyy-mm-dd): {current_date}')   

def return_date():
    with open(file_path,"r") as file:
        for line in file:
            return line



#change_date(3)
#set_today()
#print(return_date())
#print_date()