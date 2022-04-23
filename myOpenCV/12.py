# Resizing the image using cv2.INTER_CUBIC

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)

# Reducing the size using cv2.INTER_LINEAR interpolation

reduced=cv2.resize(img,None,fx=0.75,fy=0.75,interpolation=cv2.INTER_CUBIC) # Image is reduced to 75% of the original one
cv2.imshow('Reduced image',reduced)
cv2.waitKey(0)

# Increasing the size using cv2.INTER_LINEAR interpolation

zoomed=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC) # Image is zoomed to 200% of the original one
cv2.imshow('Zoomed image',zoomed)
cv2.waitKey(0)

# original=cv2.resize()

cv2.destroyAllWindows()
