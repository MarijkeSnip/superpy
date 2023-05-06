import matplotlib.pyplot as plt
#import numpy as np
from date import now
from revenue import total_revenue_per_month

#provides a line chart with the profit and revenue over given dates
def revenue_graphic(date1, date2=now):

    #dataframe wihth revenue per month
    df_revenue = total_revenue_per_month(date1, date2)

    #styling
    ax = df_revenue.plot(lw=2, colormap='jet', marker='.', markersize=10, title='Revenue per month')
    ax.set_xlabel("year-month")
    ax.set_ylabel("revenue")
    
    plt.show()

