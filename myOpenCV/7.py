# Arithmetic operations on images

# cv2.add(img1,img2) -- This directly adds up image pixels in the two images. Both the images should have same shape.

import cv2

img1=cv2.imread('lena.jpg')
print(img1.shape)
img2=cv2.imread('img2.jpg')
print(img2.shape)
opimg=cv2.add(img1,img2)

cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

B,G,R=cv2.split(img1)

opimg=cv2.add(B,R)
cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

opimg=cv2.add(B,G)
cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

opimg=cv2.add(G,R)
cv2.imshow('Result Image',opimg)
cv2.waitKey(0)

cv2.destroyAllWindows()

# But adding the pixels is not an ideal situation. So, we use cv2.addweighted()
