# cv2.subtract(img1,img2) -- This directly subtracts image pixels in the two images.

import cv2

img1=cv2.imread('lena.jpg')
print(img1.shape)
img2=cv2.imread('img2.jpg')
print(img2.shape)
opimg=cv2.subtract(img1,img2)

cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

B,G,R=cv2.split(img1)

opimg=cv2.subtract(B,R)
cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

opimg=cv2.subtract(B,G)
cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

opimg=cv2.subtract(G,R)
cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

cv2.destroyAllWindows()
