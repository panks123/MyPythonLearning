# Image pyramid

# The pyrUp() function increases the size to double of its original size and pyrDown()
# function decreases the size to half. If we keep the original image as a base image and
# go on applying pyrDown function on it and keep the images in a vertical stack, it will
# look like a pyramid. The same is true for upscaling the original image by pyrUp function.

import cv2

img=cv2.imread('lena.jpg')
print(img.shape)
smaller=cv2.pyrDown(img)
print(smaller.shape)

larger=cv2.pyrUp(img)
print(larger.shape)

cv2.imshow('Smaller',smaller)
cv2.imshow('Original',img)
cv2.imshow('Larger',larger)

cv2.waitKey(0)

resized_to_original=cv2.resize(larger,None,fx=0.5,fy=0.5)
cv2.imshow('Resized original',resized_to_original)
cv2.imshow('Previous Original',img)

# So, if we rescale it to the original size, we lose some information and the resolution of the new image is much lower
# than the original one.

print(img.shape,resized_to_original.shape)
cv2.waitKey(0)

cv2.destroyAllWindows()