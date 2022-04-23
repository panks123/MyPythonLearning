# Drawing a line

# cv2.line() method is used
# Syntax: cv2.line(image, start_point, end_point, color, thickness)

import cv2

import numpy as np

img=np.zeros((312,312,3),dtype=np.uint8)


cv2.line(img,(0,0),(312,312),(255,0,0))
cv2.line(img,(312,0),(0,312),(0,255,0))
cv2.line(img,(156,312-50),(156,50),(0,0,255))
cv2.line(img,(50,156),(312-50,156),(0,255,255))
cv2.imshow('Line drawing',img)


cv2.waitKey(0)
cv2.destroyAllWindows()