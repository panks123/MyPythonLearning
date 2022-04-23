# cv2.addweighted()

# Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
#
# Parameters:
# img1: First Input Image array(Single-channel, 8-bit or floating-point)
# wt1: Weight of the first input image elements to be applied to the final image
# img2: Second Input Image array(Single-channel, 8-bit or floating-point)
# wt2: Weight of the second input image elements to be applied to the final image
# gammaValue: Measurement of light

import cv2

img1=cv2.imread('lena.jpg')
img2=cv2.imread('img2.jpg')

weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.9, 0)

cv2.imshow('Weighted Sum Image',weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()
