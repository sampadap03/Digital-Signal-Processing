'''
Digital Image Processing
16 April 2020
by Sampada Petkar

Bitplane Slicing
'''

import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jfif', 0) 
fig=plt.figure(figsize=(8, 8))

for k in range(0, 8):
    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
    res = cv2.bitwise_and(plane, img)
    x = res * 255
    ax = fig.add_subplot(3,3,k+2)
    ax.title.set_text("Plane " + str(k+1))
    plt.imshow(x, cmap = "gist_gray")

ax1 = fig.add_subplot(3,3,1)
ax1.title.set_text("Input Image")
plt.imshow(img, cmap = "gist_gray")
    
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
