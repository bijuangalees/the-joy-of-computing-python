# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:09:24 2020

@author: bijuangalees
"""

str1=input("Enter the first number")
str2=input("Enter the second number")
count1=0
i=0
while(i<len(str1)):
    count1=count1+ord(str1[i])
    i=i+1
count2=0
i=0
while(i<len(str2)):
    count2=count2+ord(str2[i])
    i=i+1
if(count1==count2):
    print("These are anagrams")
else:
    print("These are not anagrams")
    