#  %cd dropbox/cusp/pui/pui2015_ds2455_hw3
import pandas as pd

bikes = pd.read_csv("july15bikes.csv", parse_dates=['starttime'])
#values 5,6 are Saturday and Sunday
days = bikes['starttime'].dt.dayofweek
bikes['dayvals'] = days

weekends = bikes[(bikes.dayvals == 5) | (bikes.dayvals == 6)] 
weekdays = bikes[(bikes.dayvals != 5) & (bikes.dayvals != 6)]

custWknds = weekends[weekends.usertype == 'Customer']
subWknds = weekends[weekends.usertype == 'Subscriber']

custWkday = weekdays[weekdays.usertype == 'Customer']
subWkday = weekdays[weekdays.usertype == 'Subscriber']

len(custWknds) # = 73035
len(subWknds) # = 156930
#2.15

len(custWkday) # = 107327
len(subWkday) # = 748384
#6.97

# could do float(len(subWknds)/len(custWknds)) but it rounds to whole #

