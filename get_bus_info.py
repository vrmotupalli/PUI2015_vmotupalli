# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:54:19 2015

@author: Mots

Full URL with my key and a bus so I can cut and paste...

http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=74c47369-4c4c-4c30-bb58-8ac0e2642d9b&Vehicle-MonitoringDetailLevel=calls&LineRef=B52
"""
import json
import sys
#import urllib2
import urllib.request as urllib2
import csv

if __name__=='__main__':
    
    #input variables    
    key = sys.argv[1]  
    busID = sys.argv[2]    
    
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, busID)
    
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    #Py3 syntax: with open(filename, 'w', newline='') as csvFile:    
    
    with open(sys.argv[3], 'w', newLine='') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude','Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        
        for i in buses:
            lat  = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            #author note, long is reserved
            lon  = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if i['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                stop = 'N/A'
                status = 'N/A'
            else:
                StopName = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                StopStatus = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            writer.writerow([lat,lon,stop,status])
