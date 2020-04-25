# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:35:12 2020

@author: bijuangalees
"""

import csv
with open('route.csv','r') as f:
    reader=csv.reader(f)
    
    for row in reader:
        lat= float (row[0])
        long=float (row[1])
        print(lat)
        print(long)
        print(lat + long)
        