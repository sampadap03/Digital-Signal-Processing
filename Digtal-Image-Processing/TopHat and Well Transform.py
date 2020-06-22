'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Morphological Transformtion - TopHat and Well 
'''


import cv2
import numpy as np


image = cv2.imread('tulips.jfif', 0)
#image=cv2.resize(image,(300,300),interpolation=cv2.INTER_AREA)
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
            
        

def subtract(image1,image2,result):
    for i in range (0,ht-1):
        for j in range (0,wd-1):
            if(image1[i][j]>image2[i][j]):
                result[i][j]=image1[i][j]-image2[i][j]
            else:
                result[i][j]=image2[i][j]-image1[i][j]
            
################tophat####################
gray_erosion(image)
gray_dilation(newimg_e)
#cv2.imshow('opening',newimg_e)

newimg_tp = np.zeros([ht,wd],dtype=np.uint8)
subtract(image,newimg_e,newimg_tp)
cv2.imshow('top_hat',newimg_tp)
###############well#####################
gray_dilation(image)
gray_erosion(newimg_e)

newimg_w = np.zeros([ht,wd],dtype=np.uint8)
subtract(image,newimg_e,newimg_w)
cv2.imshow('well',newimg_w)

#all rights are reserved to author.


