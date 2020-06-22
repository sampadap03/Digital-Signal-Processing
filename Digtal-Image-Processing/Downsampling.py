'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Pixelwise downsampling of Image
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('dog.jfif', 0)
fig=plt.figure()

ht,width=image.shape
x=int(width/2)
y=int(ht/2)

newimg=np.zeros([ht,width,3],dtype=np.uint8)

newimg4=np.zeros([int(y/2),int(x/2),3],dtype=np.uint8)

i=0
while(i<ht-1):
    j=0
    k=0
    
    while j<width-1:
        newimg[i][k]=image[i][j]
        newimg[i+1][k]=image[i][j]
        newimg[i][k+1]=image[i][j]
        newimg[i+1][k+1]=image[i][j]
        k=k+2;
        j=j+2;

    i=i+2

ax1 = fig.add_subplot(2,2,2)
ax1.title.set_text("Downsampled by 2")
plt.imshow(newimg, cmap = "gist_gray")

i=0
while i<ht-3:
    j=0
    k=0
    
    while j<width-3:
        for x in range (0,3):
            for y in range (0,3):
                newimg[i+x][k+y]=image[i][j]    
        k=k+4;
        j=j+4;

    i=i+4

ax2 = fig.add_subplot(2,2,3)
ax2.title.set_text("Downsampled by 4")
plt.imshow(newimg, cmap = "gist_gray")

i=0
while i<ht-7:
    j=0
    k=0
    
    while j<width-7:
        for x in range (0,7):
            for y in range (0,7):
                newimg[i+x][k+y]=image[i][j]    
        k=k+8;
        j=j+8;

    i=i+8

ax3 = fig.add_subplot(2,2,4)
ax3.title.set_text("Downsampled by 8")
plt.imshow(newimg, cmap = "gist_gray")

ax4 = fig.add_subplot(2,2,1)
ax4.title.set_text("Input image")
plt.imshow(image, cmap = "gist_gray")

plt.show()

#rights are reserved to author.
