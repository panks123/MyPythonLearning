# Image resizing / scaling

# To increase or decrease the size of the image

# OpenCV provides us several interpolation methods for resizing an image.

# 1.cv2.INTER_LINEAR: This is primarily used when zooming is required.
#                      This is the default interpolation technique in OpenCV.

# 2.cv2.INTER_CUBIC: This is slow but more efficient.

# 3.cv2.INTER_AREA: This is used when we need to shrink an image.

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)

# Reducing the size using cv2.INTER_LINEAR interpolation

reduced=cv2.resize(img,None,fx=0.75,fy=0.75) # Image is reduced to 75% of the original one
cv2.imshow('Reduced image',reduced)
cv2.waitKey(0)

# Increasing the size using cv2.INTER_LINEAR interpolation

zoomed=cv2.resize(img,None,fx=2,fy=2) # Image is reduced to 75% of the original one
cv2.imshow('Zoomed image',zoomed)
cv2.waitKey(0)

cv2.destroyAllWindows()

