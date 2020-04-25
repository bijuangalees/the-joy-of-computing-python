# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:41:25 2020

@author: bijuangalees
"""





#a a is the matrix(is the list of list )
def spiral(m,n,a):
    k=0
    l=0
   
    
    '''
    k=index of starting row
    l=index of starting column
    '''
    while(k<m and l<n):
      
          
        #Printing  the first row fromthe remaining rows
        for i in range(l,n):
            
           print(a[k][i],end=" ")
        
        k+=1
     
        
        #Printing the last colum from the remaining column
        for i in  range(k,m):
            
            print(a[i][n-1],end=" ")
            
        n-=1
      
        
        
        #Printing the last row from remaining rows
        if(k<m):
            for i in range(n-1,l-1,-1):
               
                print(a[m-1][i],end=" ")
                
        m-=1
       
        
        if(l<n):
            #Printing the first column from the remaining columns
            for i in range(m-1,k-1,-1):
                
                print(a[i][l],end=" ")
            l+=1
            
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
    
    
spiral(4,4,a)
        
                
                
                
                
            
    