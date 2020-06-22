'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Laplacian Masking
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('dog.jfif')

image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('original',image)
ht,width=image.shape
lp=[[0,-1,0],[-1,4,-1],[0,-1,0]]
k=np.zeros([ht,width],dtype=float)

temp=k[0][0]
for i in range (1,ht-1):
    for j in range (1,width-1):
        temp=0
        for x in range(0,3):
            for y in range(0,3):
                temp=temp+image[i-1+x][j-1+y]*lp[x][y]
                if(temp<0):
                    k[i][j]=0
                else:
                    k[i][j]=temp;
   
x=np.amax(k)
print(x)
for i in range (0,ht):
    for j in range(0,width):
        image[i][j]=np.uint8(k[i][j]*255/x)
cv2.imshow('Laplacian',image)

#all rights are reserved to author.
