#  %cd dropbox/cusp/pui/pui2015_ds2455_hw3
import pandas as pd

def riderprops(csv):

	bikes = pd.read_csv(csv, parse_dates=['starttime'])
	#values 5,6 are Saturday and Sunday
	days = bikes['starttime'].dt.dayofweek
	bikes['dayvals'] = days

	weekends = bikes[(bikes.dayvals == 5) | (bikes.dayvals == 6)] 
	weekdays = bikes[(bikes.dayvals != 5) & (bikes.dayvals != 6)]

	custWknds = weekends[weekends.usertype == 'Customer']
	subWknds = weekends[weekends.usertype == 'Subscriber']

	custWkday = weekdays[weekdays.usertype == 'Customer']
	subWkday = weekdays[weekdays.usertype == 'Subscriber']

	print 'Weekend customers = %s' % (len(custWknds))
	print 'Weekend subscribers = %s' % (len(subWknds)) 
	print 'Weekday customers = %s' % (len(custWkday))
	print 'Weekday subscribers = %s' % (len(subWkday))


# For July 2015:
# cust wknds: 73035
# sub wknds: 156930
# ratio = 2.15

# cust wkdys: 107327
# sub wkdys: 748384
# ratio = 6.97

# For Feb 2015:
# cust wknds: 1054
# sub wknds: 39783
# ratio = 37.74

# cust wkdy: 1211
# sub wkdy: 154882
# ratio =  127.89