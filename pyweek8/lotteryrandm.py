# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 08:54:35 2020

@author: bijuangalees
"""

import random
account=0
for i in range(365):
    
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
   # print("Bet:",bet)
    
    #print("lucky_draw:",lucky_draw)
    
    
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
        
print("Amount in your account",account)