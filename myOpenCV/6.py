# Color space and how to separate the color space from the image

# What is color space?

# Color spaces are a way to represent the color channels present in the image that gives the image that particular hue.
# There are several different color spaces and each has its own significance.
# Some of the popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black),
# HSV (Hue, Saturation, Value), etc.

# OpenCV’s default color space is RGB. However, it actually stores color in the BGR format.

import cv2

img=cv2.imread('lena.jpg')

# Separating the color channels

B,G,R=cv2.split(img)

print(B)

cv2.imshow('Original',img)
cv2.waitKey(0)

cv2.imshow('Blue',B)
cv2.waitKey(0)

cv2.imshow('Green',G)
cv2.waitKey(0)

cv2.imshow('Red',R)
cv2.waitKey(0)

cv2.destroyAllWindows()