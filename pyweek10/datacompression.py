# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:48:14 2020

@author: bijuangalees
"""

import numpy as np
#x=np.array([1.0,2.0])
#print(x.dtype)
#x=np.array([1,2], dtype=np.int64)
#print(x.dtype)
a=np.array([[1,2],[3,4]], dtype = np.float64)

b=np.array([[5,6],[7,8]], dtype= np.float64)
print(a)
print(b)
#print(a+b)
print(np.subtract(a,b))
print(np.multiply(a,b))

print(np.transpose(a))