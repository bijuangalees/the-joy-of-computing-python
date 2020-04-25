# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 08:19:29 2020

@author: bijuangalees
"""
import random

bet=int(input("you bet from 1 to 10"))
lucky_draw=random.randint(1,10)
print(lucky_draw)
account=0

if bet==lucky_draw:
    account=account+900-100
else:
    account=account-100
    
print(account)


