# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:19:35 2015

@author: Eee
"""

import csv
"""out=open("data.csv","rb")
data=csv.reader(out)"""

with open("data.csv", "r") as data:
    datareader = csv.reader(data)

    #datareader=[row for row in data]
    #data=[[row[0], eval(row[1]),eval(row[2])] for row in data]
    """datalist = []
    for row in datareader:
        if len (row) != 0:
            datalist = datalist + [row]"""
    #new_data=[[row[0],row[2],row[4]] for row in data]
    new_data=[[row[0],int(row[2])+int(row[4])] for row in data]
data.close()

print (new_data)
with open("new_data.csv", "w") as data2:
    datawriter2 = csv.writer(data2)
    datawriter2.writerow([new_data])
