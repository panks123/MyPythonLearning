# Image Blurring (Image Smoothing) - Next to 14.py

# Image blurring is achieved by convolving the image with a low-pass filter kernel.
# It is useful for removing noise. It actually removes high frequency content (eg: noise, edges)
# from the image. So edges are blurred a little bit in this operation (there are also blurring
# techniques which don't blur the edges). OpenCV provides four main types of blurring techniques.

# 1. Averaging - This is done by the function cv.blur() or cv.boxFilter()

# This is done by convolving an image with a normalized box filter. It simply takes the average of all
# the pixels under the kernel area and replaces the central element.
# e.g. of a normalized 3x3 box filter 1/9[[1,1,1],
#                                         [1,1,1],
#                                         [1,1,1]]

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original',img)

avg_blur=cv2.blur(img,(5,5)) # (3,3) is the box (i.e. kernel) size

cv2.imshow('Averaging',avg_blur)

# 2. Gaussian Blurring - It is done with the function, cv.GaussianBlur()

# In this method, instead of a box filter, a Gaussian kernel is used.  We should specify the
# width and height of the kernel which should be positive and odd. We also should specify the
# standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is
# specified, sigmaY is taken as the same as sigmaX. If both are given as zeros, they are
# calculated from the kernel size. Gaussian blurring is highly effective in removing Gaussian noise from an image.

gaussian_blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('Gaussian', gaussian_blur)

# 3. Median Blurring - function cv.medianBlur() is used

# It takes the median of all the pixels under the kernel area and the central element is replaced with this median
# value.This is highly effective against salt-and-pepper noise in an image. Interestingly, in the above filters, the
# central element is a newly calculated value which may be a pixel value in the image or a new value. But in median
# blurring,the central element is always replaced by some pixel value in the image. It reduces the noise effectively.
# Its kernel size should be a positive odd integer.

median_blur=cv2.medianBlur(img,5)  # here 5 means 5x5 kernel
cv2.imshow('Median',median_blur) # We can see that it is much smoother than the above two

# 4. Bilateral Filtering - cv.bilateralFilter() is used

# Gaussian filter takes the neighbourhood around the pixel and finds its Gaussian weighted average.
# This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering.
#  It doesn't consider whether pixels have almost the same intensity. It doesn't consider whether a pixel
#  is an edge pixel or not. So it blurs the edges also, which we don't want to do.

# Bilateral filtering is highly effective in noise removal while keeping edges sharp. Hence it preserves the edges

bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral',bilateral)

# So we can see that bilateral filter provides highest level of smoothness in the image
# as well as it preserves the edges.

cv2.waitKey(0)
cv2.destroyAllWindows()
