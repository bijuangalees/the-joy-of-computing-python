# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:13:53 2020

@author: bijuangalees
"""

def fact(n):
    if(n==1):
        return(1)
    elif(n>1):
        return(n*fact(n-1))
    else:
        print("in correct n")