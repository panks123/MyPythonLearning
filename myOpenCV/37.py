# Drawing a rectangle

# cv2.rectangle() method is used
# Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)

import cv2
import numpy as np

img=np.zeros((312,312,3),np.uint8)

cv2.rectangle(img,(50,50),(312-50,312-50),(0,255,0))
cv2.rectangle(img,(100,100),(312-100,312-100),(255,255,0))
cv2.rectangle(img,(150,150),(312-150,312-150),(0,255,255),-1)

cv2.imshow('Rectangle drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()