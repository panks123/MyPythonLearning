# Bitwise operations

import cv2

img1=cv2.imread('img3.jpg')
cv2.imshow('Input image 1',img1)
cv2.waitKey(0)

img2=cv2.imread('img4.png')
cv2.imshow('Input image 2',img2)
cv2.waitKey(0)


# AND operation
result=cv2.bitwise_and(img1,img2,mask=None)
cv2.imshow('AND',result)
cv2.waitKey(0)

# OR operation
result=cv2.bitwise_or(img1,img2,mask=None)
cv2.imshow('OR',result)
cv2.waitKey(0)

# XOR operation
result=cv2.bitwise_xor(img1,img2,mask=None)
cv2.imshow('XOR',result)
cv2.waitKey(0)

# NOT operation
result=cv2.bitwise_not(img2,mask=None)
cv2.imshow('NOT',result)
cv2.waitKey(0)

cv2.destroyAllWindows()

