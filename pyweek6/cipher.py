# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:17:38 2020

@author: bijuangalees
"""
import string
dict={}
data=""
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)

with open("read_file_cipher.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
            file.write(data)
            print(data)
file.close           