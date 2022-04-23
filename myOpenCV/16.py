# Grayscaling of images

# Grayscaling is the process of converting an image from other color spaces e.g RGB, CMYK, HSV, etc. to shades of gray.
# It varies between complete black and complete white.

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original Image',img)
print(img.shape)


grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image',grayscale)
print(grayscale.shape) # So we can see that RGB color channel dimension is not present in the grayscale image
print(grayscale)

# Second method is to directly read the image as the grayscale image
grayscale1=cv2.imread('lena.jpg',0)
cv2.imshow('Grayscale-Image',grayscale1)
print(grayscale1.shape)
cv2.waitKey(0)

cv2.destroyAllWindows()