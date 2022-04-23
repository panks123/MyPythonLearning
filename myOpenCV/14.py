# Image blurring

# Image Blurring refers to making the image less clear or distinct.
# It is done with the help of various low pass filter kernels. An image is convolved with the low pass filter
# for image blurring.

# It is used for image smoothening, It helps in Noise removal, It helps in hiding the details when necessary.

import cv2
import numpy as np

img=cv2.imread('lena.jpg')
cv2.imshow('Original image',img)

# Creating a 3x3 kernel
kernel1=np.ones((3,3),dtype=np.float32)/9

# OpenCV provides a function cv2.filter2D() to convolve a kernel with an image.

filter1=cv2.filter2D(img,-1,kernel1)
cv2.imshow('3x3 blurring',filter1)

print(img,"\n\n++++++++++++++++++++++\n\n",filter1)


# Creating a 5x5 kernel
kernel2=np.ones((5,5),dtype=np.float32)/25

filter2=cv2.filter2D(img,-1,kernel2)
cv2.imshow('5x5 blurring',filter2)

# Creating a 7x7 kernel
kernel3=np.ones((7,7),dtype=np.float32)/49

filter3=cv2.filter2D(img,-1,kernel3)
cv2.imshow('7x7 blurring',filter3)

# So we can see that blurring effect goes on increasing by increasing the size of the kernel matrix

cv2.waitKey(0)
cv2.destroyAllWindows()