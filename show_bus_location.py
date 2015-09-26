# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:14:47 2015

@author: Mots


Full URL with my key and a bus so I can cut and paste...

http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=74c47369-4c4c-4c30-bb58-8ac0e2642d9b&Vehicle-MonitoringDetailLevel=calls&LineRef=B52
"""

import json
import sys
#import urllib2
import urllib.request as urllib2

if __name__=='__main__':

    # input variables    
    key = sys.argv[1]  
    busID = sys.argv[2]  
     
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, busID)
    
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    
    """    
    Path is from CodeBeautify's JSON viewer www.codebeautify.com/jsonviewer
    I looked at some class repos to figure out the syntax for calling a path
    """
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    print ("Bus Line : %s" % busID)      
    print ("Number of Active Buses : %d" % (len(buses)))
    for i in range(len(buses)):
        locations = buses[i]['MonitoredVehicleJourney']["VehicleLocation"]
        lat = locations['Latitude']
         #author note, long is reserved
        lon = locations['Longitude']
        print ("Bus %i is at latitude %f and longitude %f" % (i, lat, lon))
