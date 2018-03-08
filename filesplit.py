# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:25:29 2018

@author: erik
"""
#string = '2018-02-27T20:00:03.019600Z,58.577,78.132,11.406,TekLinks\n'
writefile = open('workingfile.csv', 'w')

writefile.write('date,UTCtime,ping,download,upload,server\n')

with open('speedtest.csv') as file:
    for line in file:
        try:
            stringsplit = line.split(sep='Z')
            timestamp = stringsplit[0]  
            timesplit = timestamp.split(sep='T')
            results = timesplit[0] + ',' + timesplit[1] + stringsplit[1]
            writefile.write(results)
        except:
            pass
        
writefile.close()        