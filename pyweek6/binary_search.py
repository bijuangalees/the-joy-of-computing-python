# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:52:33 2020

@author: bijuangalees
"""

def binary_search(l,x,start,end):
    #Base Case:1 element
    if start==end :
        if l[start]==x:
            return start
        else:
            return -1
    else:
         #divide the array into halues
         mid=int((start+end)/2)
         if l[mid]==x:
             return mid
         elif l[mid]>x:
             #left half
             return binary_search(l,x,start,mid-1)
         else:
             return binary_search(l,x,mid+1,end)
         
 l= [1,14,48,49,52,75,89,95]
 x=int(input("Enter the search key:"))     
index=binary_search(l,x,0,len(l)-1)
if index==-1:
    print(x,'not find')
else:
print(x,'is not find',index+1)       
         
                
    
    