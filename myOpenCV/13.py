# Resizing the image using cv2.INTER_AREA

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)

resized=cv2.resize(img,(412,312),interpolation=cv2.INTER_AREA)
cv2.imshow('Resized image - 412 x 312',resized)
cv2.waitKey(0)

cv2.destroyAllWindows()
