import argparse
import datetime
from date import print_date, advance_days, set_today, change_date #, print_date, set_current_date
from purchase import register_purchase
from sales import sell_product
from inventory import show_inventory, export_inventory
from revenue import total_revenue
from profit import total_profit
from graphic import revenue_graphic

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

#create ArgumentParser 
parser = argparse.ArgumentParser(description='Superpy data')

#Add parsers..
subparser = parser.add_subparsers(dest="command", required=True)

#Date - Add parsers and arguments
show_date = subparser.add_parser("show-date", help="prints set system date")
date_today = subparser.add_parser("date-today", help="Set system date to today, format YYYY/MM/DD")
advance_date = subparser.add_parser("advance-date", help="Offset the system date by a number of days from system date")
set_date = subparser.add_parser("set-date", help="Set system date to given date, format YYYY/MM/DD")

advance_date.add_argument("--d", "--days", type=int, help="Enter --d number of days", required=True)
set_date.add_argument("--d","--date", type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), metavar="", help = "Enter --d date: Format YYYY-MM-DD", required=True) 

#Purchases - Add parsers and arguments
purchase = subparser.add_parser("buy", help="Register purchases, buy date is set system date")

purchase.add_argument("--n", "--productname", type = str.lower, metavar="", help = "Enter --n productname, enclose double words with double quotation marks",  required=True) 
purchase.add_argument("--p","--price", type = float, metavar="", help = "Enter --p purchace price: Format 4.53", required=True)
purchase.add_argument("--e","--expires", type = str, metavar="", help = "Enter --e expiration date: Format YYYY-MM-DD", required=True) 

#Sales - Add parsers and arguments
sale = subparser.add_parser("sale", help="Register sales, sell date is set system date")

sale.add_argument("--n", "--productname", type= str.lower , metavar="", required=True, help="Enter --n productname, enclose double words with double quotation marks")
sale.add_argument("--p", "--price", type= float, metavar="", required=True, help= "Enter --p sell price: Format 0.75")

#Inventory - Add parsers and arguments
inventory = subparser.add_parser("show-inventory", help="Shows the inventory on given date (default = today)")
inventory_export = subparser.add_parser("export-inventory", help="exports the inventory on given date to a csv or excel file(default = today)")

inventory.add_argument("--d", "--date", nargs = '?', const = datetime.date.today(), type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), metavar="", help="Enter --d date: Format yyyy-mm-dd" )
inventory_export.add_argument("--f", "--format", metavar="", required=True, choices=['c', 'x'], help="Enter the desired format: csv(c) or excel(x)" )
inventory_export.add_argument("--d", "--date", nargs = '?', const = datetime.date.today(), type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), metavar="", help="Enter --d date: Format yyyy-mm-dd" )

#Revenue - Add parsers and arguments
revenue_total = subparser.add_parser("revenue-total", help="Shows the total revenue from date1 till date2: format yyyy-mm-dd (default = today)")

revenue_total.add_argument("--d1","--date-from", type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), required=True, help="Enter date from: format yyyy-mm-dd")
revenue_total.add_argument("--d2","--date-till", nargs = '?', const = datetime.date.today(), type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), required=True, help="Enter date till: format yyyy-mm-dd (default=today)")

#revenue visual parser and arguments
revenue_visual = subparser.add_parser("revenue-visual", help="Shows the total revenue from date1 till date2 in a graphic: format yyyy-mm-dd (default = today)")

revenue_visual.add_argument("--d1","--date-from", type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), required=True, help="Enter date from: format yyyy-mm-dd")
revenue_visual.add_argument("--d2","--date-till", nargs = '?', const = datetime.date.today(), type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), required=True, help="Enter date till: format yyyy-mm-dd (default=today)")

#Profit - Add parsers and arguments 
profit_total = subparser.add_parser("profit-total", help="Shows the total profit from date1 till date2: format yyyy-mm-dd (default = today)")

profit_total.add_argument("--d1","--date-from", required=True, nargs = '?', const = datetime.date.today(), type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), help="Enter date from: format yyyy-mm-dd")
profit_total.add_argument("--d2","--date-till", nargs = '?', const = datetime.date.today(), type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(), required=True, help="Enter date till: format yyyy-mm-dd (default=today)")




args = parser.parse_args()


#date commands
if args.command == "show-date":
    show_date.set_defaults(function=print_date())

if args.command == "advance-date":
    advance_date.set_defaults(function=advance_days(args.d))

if args.command == "date-today":
    date_today.set_defaults(function=set_today())

if args.command == "set-date":
    set_date.set_defaults(function=change_date(args.d))

#Purchase commands
if args.command == "buy":
    purchase.set_defaults(
        function = register_purchase(
            args.n,
            args.p,
            args.e))

#Sale commands
if args.command == "sale":
    sale.set_defaults(
        func=sell_product(
            args.n,
            args.p))

#inventory commands
if args.command == "show-inventory":
    inventory.set_defaults(
        func=show_inventory(
            args.d,))

if args.command == "export-inventory":
    inventory.set_defaults(
        func=export_inventory(
            args.f,
            args.d,))


#revenue commands
if args.command == "revenue-total":
    revenue_total.set_defaults(
        func=total_revenue(
            args.d1,
            args.d2,))

#revenue visuel commands
if args.command == "revenue-visual":
    revenue_visual.set_defaults(
        func=revenue_graphic(
            args.d1,
            args.d2,))

#profit commands
if args.command == "profit-total":
    profit_total.set_defaults(
        func=total_profit(
            args.d1,
            args.d2,))
