# Drawing a circle

# cv2.circle() method is used
# Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)

import cv2
import numpy as np

img=np.zeros((312,312,3),np.uint8)

cv2.circle(img,(156,156),25,(0,255,0),-1)
cv2.circle(img,(156,156),50,(0,0,255))
cv2.circle(img,(156,156),75,(255,0,0))
cv2.circle(img,(156,156),100,(0,255,0))
cv2.circle(img,(156,156),125,(0,0,255),)

cv2.imshow('Circle drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
