# superpy

This is Superpy.

Instructions:
Download these files and place them in a directory:
- super.py
- sales.py
- purchase.py
- inventory.py
- revenue.py
- profit.py
- date.py
- graphic.py
- date.txt
- bought.csv
- sell.csv


Open CLI and open the directory where you placed the downloaded files.
All commands are registered in super.py, so that's the file you will use.

Before registering purchases and sales, check the set system date via show-date. If necessary, adjust it with set-date or date-today.
The set date is used as the purchase and sale date.

Via the command python super.py -h you can see all options with the help information in CLI.

Examples per function:


show-date
	The set systemdate is displayed.

	input: python super.py show-date
	output: Date is currently set to (yyyy-mm-dd)
	

advance-date
	The system date will be changed by the number of days entered compared to the set system date (example: 2023-05-05).

	input: python syper.py advance-date --d -2
	output: Date is set to 2023-05-03
	
set-date
	The system date will be changed to the given date (example: 2023-05-05).

	input: python syper.py set-date --d 2023-05-05
	output: Date is set to 2023-05-05

date-today
	The date is set to today.

	input: python super.py date-today
	output: Date is set to (yyyy-mm-dd (today))

buy
	register bought products. Enter productname, price and expiration date.
	The product will be added to the csv file with bought items. The bought date is automatically set to the set date by user (see show-date).

	input: python super.py buy --n orange --p 0.23 --e 2023-05-10
	output: orange is added to bought items

sale
	register sold products. Enter productname and price.
	The product will be added to the csv file with sold items. The sell date is automatically set to the set date by user (see show-date).

	input: python super.py sale --n orange --p 0.23
	output: orange is added to sold items

show-inventory
	shows the inventory on given date (default = today)
	
	input: python super.py show inventory –-d
	output: inventory for today

	input: python super.py show inventory –-d 2023-05-04
	output: inventory for 2023-05-04

revenue-total
	shows the revenue from date1 up till date2 (date 2 default = today).

	input: python super.py revenue-total --d1 2023-04-01 --d2 2023-05-04
	output: The total revenue from 2023-04-01 till 2023-05-04 is {total}

	input: python super.py revenue-total –-d1 2023-05-01 –-d2
	output: The total revenue from 2023-04-01 till {today} is {total}

revenue-visual
	shows the revenue from date1 up till date2 (date 2 default = today) in a line chart.

	input: python super.py revenue-total --d1 2023-04-01 --d2 2023-05-04
	output: line chart with revenue per month

	input: python super.py revenue-total -–d1 2023-05-01 –-d2
	output: line chart with revenue per month

profit-total
	shows the profit from date1 up till date2 (date 2 default = today).

	input: python super.py profit-total –-d1 2023-04-01 –-d2 
	output: The total profit from 2023-04-01 till {today} is {total}

	input: python super.py profit-total –-d1 2023-04-01 –-d2 2023-05-31
	output: The total profit from 2023-04-01 till 2023-05-31 is {total}
