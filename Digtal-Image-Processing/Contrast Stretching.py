'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Contrast stretching
'''

import cv2
import numpy as np
img = cv2.imread('paw.jfif')

original = img.copy()
cv2.imshow("original_LH", original)

xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
cv2.imshow("Output - LH", img)
img2 = cv2.imread('flower.jfif')

original2 = img2.copy()
cv2.imshow("original HL", original2)

fp2 = [0, 64, 128, 192, 255]
xp2 = [0, 20, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp2, fp2).astype('uint8')
img2 = cv2.LUT(img2, table)
cv2.imshow("Output - HL", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#all rights are reserved to author.
