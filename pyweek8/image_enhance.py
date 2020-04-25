# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:06:21 2020

@author: bijuangalees
"""

#Image enhancement CLAHE
import cv2
#Read the image
img=cv2.imread('crime.png')
#preparation for CLAHE
clahe=cv2.createCLAHE()
#convert to gray scale image
gray_img=cv2.cvtColor(img,Color_BGR2GRAY)

#Apply enhancement
enh_img=clahe.apply(gray_img)

cv2.imwrite('enhanced.png',enh_img)

print('Done enhancing')

