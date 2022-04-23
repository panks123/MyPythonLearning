# cv2.merge()--cv2.merge takes single channel images and combines them to make a multi-channel image

import cv2
import numpy as np

img=cv2.imread('lena.jpg')
cv2.imshow('Original',img)

b,g,r=cv2.split(img)
print(b.shape)

print(img)
print('++++++++++++++++++++++++++++++++++++++++\n\n')
print(b)
print('++++++++++++++++++++++++++++++++++++++++\n\n')
print(g)
print('++++++++++++++++++++++++++++++++++++++++\n\n')
print(r)

zeros=np.zeros(img.shape[:2],dtype='uint8')

cv2.imshow('Red Channel',cv2.merge([zeros,zeros,r]))
cv2.imshow('Green Channel',cv2.merge([zeros,g,zeros]))
cv2.imshow('Blue Channel',cv2.merge([b,zeros,zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
