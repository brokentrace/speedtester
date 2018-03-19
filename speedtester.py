#!/usr/bin/env python

import speedtest

servers = [4795] #use Teklinks in Birmingham,AL
# If you want to test against a specific server
# servers = [1234]

file = '/etc/cron.d/speedtest.csv' #change this to your csv path

#print "Starting speedtest......"

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()

results = s.results.dict()
server = results['server']

download = round((results['download'] / 1000000),3)
upload = round((results['upload'] / 1000000),3)

entry = str(results['timestamp']) + "," +str(results['ping']) + "," + str(download) + "," + str(upload) + "," + str(server['sponsor']+ '\n')

workfile = open(file, 'a')
workfile.write(entry)
workfile.close

#print "Speedtest Results"
#print "Timestamp: " + str(results['timestamp'])
#print "Ping: " + str(results['ping'])
#print "Download: " + str(download)
#print "Upload: " + str(upload)
#print "Server: " + server['sponsor']
#print entry
