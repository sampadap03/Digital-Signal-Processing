'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Morphological Transformtion on binary Images
Erosion, Dilation, Opening, Closing
'''

import cv2
import numpy as np

image = cv2.imread('sampada.png', 0)
cv2. imshow('original', image)

ht,wd =image.shape
mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

newimg_e = np.zeros([ht,wd,3],dtype=np.uint8)

for i in range (0, ht -1):
    for j in range (0, wd - 1):
        flag = ((mask[0][0] & image[i-1][j-1]) & (mask[0][1] & image[i-1][j]) & (mask[0][0] & image[i-1][j+1])
                & (mask[1][0] & image[i][j-1]) & (mask[1][1] & image[i][j]) & (mask[1][0] & image[i][j+1])
                & (mask[2][0] & image[i+1][j-1]) & (mask[2][1] & image[i+1][j]) & (mask[2][0] & image[i+1][j+1]))

        if flag == 1:
            newimg_e[i][j] = 255
            
        else:
            newimg_e[i][j] = 0
            
cv2.imshow('erosion', newimg_e)

flag = 0
mask_d = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

newimg_d = np.zeros([ht,wd,3],dtype=np.uint8)

for i in range (0, ht -1):
    for j in range (0, wd - 1):
        flag = ((mask_d[0][0] | image[i-1][j-1]) | (mask_d[0][1] | image[i-1][j]) | (mask_d[0][0] | image[i-1][j+1])
                | (mask_d[1][0] | image[i][j-1]) | (mask_d[1][1] | image[i][j]) | (mask_d[1][0] | image[i][j+1])
                | (mask_d[2][0] | image[i+1][j-1]) | (mask_d[2][1] | image[i+1][j]) | (mask_d[2][0] | image[i+1][j+1]))
       
        if flag != 0:
            newimg_d[i][j] = 255
            
        else:
            newimg_d[i][j] = 0
            
cv2.imshow('dilation', newimg_d)

flag = 0
newimg_o = np.zeros([ht,wd,3],dtype=np.uint8)

for i in range (0, ht -1):
    for j in range (0, wd - 1):
        flag = ((mask_d[0][0] | newimg_e[i-1][j-1][0]) | (mask_d[0][1] | newimg_e[i-1][j][0]) | (mask_d[0][0] | newimg_e[i-1][j+1][0])
                | (mask_d[1][0] | newimg_e[i][j-1][0]) | (mask_d[1][1] | newimg_e[i][j][0]) | (mask_d[1][0] | newimg_e[i][j+1][0])
                | (mask_d[2][0] | newimg_e[i+1][j-1][0]) | (mask_d[2][1] | newimg_e[i+1][j][0]) | (mask_d[2][0] | newimg_e[i+1][j+1][0]))
        
        if flag != 0:
            newimg_o[i][j] = 255
            
        else:
            newimg_o[i][j] = 0
            
cv2.imshow('opening', newimg_o)

newimg_c = np.zeros([ht,wd,3],dtype=np.uint8)

for i in range (0, ht -1):
    for j in range (0, wd - 1):
        flag = ((mask[0][0] & newimg_d[i-1][j-1][0]) & (mask[0][1] & newimg_d[i-1][j][0]) & (mask[0][0] & newimg_d[i-1][j+1][0])
                & (mask[1][0] & newimg_d[i][j-1][0]) & (mask[1][1] & newimg_d[i][j][0]) & (mask[1][0] & newimg_d[i][j+1][0])
                & (mask[2][0] & newimg_d[i+1][j-1][0]) & (mask[2][1] & newimg_d[i+1][j][0]) & (mask[2][0] & newimg_d[i+1][j+1][0]))

        if flag == 1:
            newimg_c[i][j] = 255
            
        else:
            newimg_c[i][j] = 0
           

cv2.imshow('closing', newimg_c)

#all rights are reserved to author.
 



