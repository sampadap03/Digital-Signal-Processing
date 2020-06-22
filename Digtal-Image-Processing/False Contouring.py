'''
Digital Image Processing
16 April 2020
by Sampada Petkar

False contouring
'''
import cv2

q=2
factor=2**(8-q)

image=cv2.imread('floww.jfif', 0)
image=cv2.resize(image,(500,300),interpolation=cv2.INTER_AREA)
cv2.imshow('Original',image)
#print(image)
def falseContour(image):
    ht,width=image.shape
    for i in range (0,ht):
        for j in range (0,width):
            image[i][j]=int(image[i][j]/factor)*factor            
  
    cv2.imshow('Quantized',image)

falseContour(image)

#all rights are reserved to author.
    
