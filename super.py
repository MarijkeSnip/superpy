import argparse
#import pandas as pd
from date import print_date, change_date, set_today #, print_date, set_current_date
from purchase import register_purchase
#from inventory import show_inventory
from sales import sell_product

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


#create ArgumentParser 
parser = argparse.ArgumentParser(description='Superpy data')

#Add parsers..
subparser = parser.add_subparsers(dest="command", required=True)

#Date - Add parsers and arguments
show_date = subparser.add_parser("show-date", help="prints date")
date_today = subparser.add_parser("date-today", help="Set system date to today, format YYYY/MM/DD")
set_date = subparser.add_parser("set-date", help="Offset the system date by a number of days")

set_date.add_argument("days", type=int)

#Purchases - Add parsers and arguments
purchase = subparser.add_parser("register-buy", help="Register the purchases")
purchases = subparser.add_parser("show-purchases", help="Shows all the purchases made")

purchase.add_argument("--n", "--productname", type = str.lower, metavar="", help = "Enter productname", nargs='+', required=True) 
#purchase.add_argument("--d","--buy-date", type = int, metavar="", help = "Format YYYY-MM-DD", required=True) #Voor nu system date ingesteld 
#purchase.add_argument("--q","--quantity", type = int, metavar="", help = "Format 2", required=True) #in voorbeeld wordt aantal niet ingevoerd, dus default op 1 gezet
purchase.add_argument("--p","--price", type = float, metavar="", help = "Purchase price: Format 4.53", required=True)
purchase.add_argument("--e","--expires", type = str, metavar="", help = "Format YYYY-MM-DD", required=True) 

#Sales - Add parsers and arguments
sales = subparser.add_parser("show-sales", help="Shows all the sales made")
sale = subparser.add_parser("register-sale", help="Register sales")

sale.add_argument("--n", "--productname", type= str.lower, metavar="", required=True, help="Enter productname", nargs='+')
#sale.add_argument("--quantity", type= int)
sale.add_argument("--p", "--price", type= float, metavar="", required=True, help= "Enter sell price: Format 0.75")

#Revenue - Add parsers and arguments
total_revenue = subparser.add_parser("show-total-revenue", help="Shows the total revenue")
date_revenue = subparser.add_parser("show-date-revenue", help="Shows the total revenue, between two dates")

date_revenue.add_argument("--firstdate", type= str)
date_revenue.add_argument("--seconddate", type= str)

#Profit - Add parsers and arguments 
total_profit = subparser.add_parser("show-total-profit", help="Shows the total profit")
date_profit = subparser.add_parser("show-date-profit", help="Shows the total profit, between two dates")

date_profit.add_argument("--firstdate", type= str)
date_profit.add_argument("--seconddate", type= str)

#Inventory - Add parsers and arguments
inventory = subparser.add_parser("report-inventory", help="Shows the currently available products, and gives the option to export as CSV or PDF")

#inventory.add_argument("-c", "--exportCSV", type= str)
#inventory.add_argument("-p", "--exportPDF", type= str)

args = parser.parse_args()


#commands
if args.command == "show-date":
    show_date.set_defaults(function=print_date())

if args.command == "set-date":
    set_date.set_defaults(function=change_date(args.days))

if args.command == "date-today":
    date_today.set_defaults(function=set_today())

#Purchase commands
if args.command == "register-buy":
    purchase.set_defaults(
        function = register_purchase(
            args.n,
            args.p,
            args.e))

#Sale commands
if args.command == "register-sale":
    sale.set_defaults(
        func=sell_product(
            args.n,
            args.p))

