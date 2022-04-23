# Transpose of an image

import cv2

img=cv2.imread('lena.jpg')
print(img.shape)
print(img)
cv2.imshow('Original',img)

trans=cv2.transpose(img)
print(trans.shape)
print(trans)
cv2.imshow('Transpose',trans)


img=cv2.imread('lena.jpg',0)
print(img.shape)
print(img)
cv2.imshow('Original Grayscale',img)

trans=cv2.transpose(img)
print(trans.shape)
print(trans)
cv2.imshow('Transpose Grayscale',trans)

# So we can see that transpose of the image matrix takes place and the image is rotated by 90 deg anticlockwise

cv2.waitKey(0)
cv2.destroyAllWindows()