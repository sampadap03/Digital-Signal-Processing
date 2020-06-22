'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Morphological Transformtion on Greyscale Images
Erosion, Dilation, Opening, Closing
'''

import cv2
import numpy as np


image = cv2.imread('tulips.jfif', 0)
cv2.imshow('original',image)
ht,wd =image.shape

mask = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

newimg_e = np.zeros([ht,wd],dtype=np.uint8)

def gray_erosion(image_in):
    #flag=0;
    image=image_in.copy()
    for i in range (1, ht -1):
        for j in range (1, wd - 1):
            flag = [mask[0][0] + image[i-1][j-1],mask[0][1]+image[i-1][j],mask[0][2]+image[i-1][j+1],
                    mask[1][0] + image[i][j-1],mask[1][1] + image[i][j],mask[1][0] + image[i][j+1],
                    mask[2][0] + image[i+1][j-1],mask[2][1] + image[i+1][j],mask[2][0] + image[i+1][j+1]]


            newimg_e[i][j] = min(flag)


def gray_dilation(image_in):
    #flag=0;
    image=image_in.copy()
    for i in range (1, ht -1):
        for j in range (1, wd - 1):
            flag = [mask[0][0] + image[i-1][j-1],mask[0][1]+image[i-1][j],mask[0][2]+image[i-1][j+1],
                    mask[1][0] + image[i][j-1],mask[1][1] + image[i][j],mask[1][0] + image[i][j+1],
                    mask[2][0] + image[i+1][j-1],mask[2][1] + image[i+1][j],mask[2][0] + image[i+1][j+1]]


            newimg_e[i][j] = max(flag)
            
        
gray_erosion(image)
cv2.imshow('Erosion',newimg_e)


gray_dilation(image)
cv2.imshow('Dilation',newimg_e)


gray_erosion(image)
gray_dilation(newimg_e)
cv2.imshow('Opening',newimg_e)

gray_dilation(newimg_e)
gray_erosion(image)
cv2.imshow('Closing',newimg_e)

#all rights are reserved to author.
