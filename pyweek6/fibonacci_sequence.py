# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:18:49 2020

@author: bijuangalees
"""

def fibonacci(n):
 
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
    
n=int(input("Enter the number:"))
a=fibonacci(n)
print(fibonacci(n))