'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Weighted average and averaging mask
'''

import cv2
import numpy as np

image = cv2.imread('flower.jfif', 0)
cv2. imshow('original', image)

ht,wd =image.shape
newimg = np.zeros([ht,wd,3],dtype=np.uint8)
newimg_w = np.zeros([ht,wd,3],dtype=np.uint8)

def average(image):
    for i in range (0, ht -1):
        for j in range (0, wd - 1):
            avg = int((int(image[i-1][j-1]) + int(image[i-1][j]) + int(image[i-1][j+1])
                       + int(image[i][j-1]) + int(image[i][j]) + int(image[i][j+1])
                       + int(image[i+1][j-1]) + int(image[i+1][j]) + int(image[i+1][j+1])) / 9)
            if(avg > 255):
                avg = 255
            newimg[i][j] =avg

    cv2. imshow('average', newimg)


def weighted(image):
    mask = [[3, 2, 3], [2, 1, 2], [3, 2, 3]]
    for i in range (0, ht -1):
        for j in range (0, wd - 1):
            w_avg = int((int(image[i-1][j-1])* mask[0][0] + int(image[i-1][j])* mask[0][1] + int(image[i-1][j+1])* mask[0][2]
                       + int(image[i][j-1])* mask[1][0] + int(image[i][j])* mask[1][1] + int(image[i][j+1])* mask[1][2]
                       + int(image[i+1][j-1])* mask[2][0] + int(image[i+1][j])* mask[2][1] + int(image[i+1][j+1]* mask[2][2])) / 9)
            if(w_avg > 255):
                w_avg = 255
            newimg_w[i][j] = w_avg

    cv2. imshow('weighted average', newimg_w)


average(image)
weighted(image)

#all rights are reserved to author.
