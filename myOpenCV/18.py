# Thresholding -

# Thresholding is a technique in OpenCV, which is the assignment of pixel values in
# relation to the threshold value provided. In thresholding, each pixel value is compared
# with the threshold value. If the pixel value is smaller than the threshold,
# it is set to 0, otherwise, it is set to a maximum value (generally 255)

# cv2.threshold is used for thresholding

# Syntax: cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)
# where
# -> source: Input Image array (must be in Grayscale(single channel)).
# -> thresholdValue: Value of Threshold below and above which pixel values will change accordingly.
# -> maxVal: Maximum value that can be assigned to a pixel.
# -> thresholdingTechnique: The type of thresholding to be applied.

import cv2
img=cv2.imread('lena.jpg',0) # Grayscale image
cv2.imshow('Original image',img)

# Simple Thresholding -- The basic Thresholding technique is Binary Thresholding.

# different Simple Thresholding Techniques are:

# cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
# cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
# cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold.
# The pixel values are set to be the same as the threshold. All other values remain the same.
# cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
# cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

print(ret)

cv2.imshow('cv2.THRESH_BINARY',thresh1)
cv2.imshow('cv2.THRESH_BINARY_INV',thresh2)
cv2.imshow('cv2.THRESH_TRUNC',thresh3)
cv2.imshow('cv2.THRESH_TOZERO',thresh4)
cv2.imshow('cv2.THRESH_TOZERO_INV',thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
