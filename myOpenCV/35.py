# Drawing ellipse

# cv2.ellipse() method is used
# Syntax: cv2.ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color
# [, thickness[, lineType[, shift]]])
# Here
# axesLength: It contains tuple of two variables containing major and minor axis of ellipse (major axis length,
# minor axis length).
# angle: Ellipse rotation angle in degrees.
# startAngle: Starting angle of the elliptic arc in degrees.
# endAngle: Ending angle of the elliptic arc in degrees.

import cv2
import numpy as np

img=np.zeros((312,312,3),np.uint8)
center=(156,156)
axesLength=(100,50)

angle=0
startAngle=0
endAngle=360
color=(0,255,0)

cv2.ellipse(img,center,axesLength,angle,startAngle,endAngle,color)

cv2.ellipse(img,center,axesLength,45,startAngle,endAngle,(0,0,255))
cv2.ellipse(img,center,axesLength,60,startAngle,endAngle,color)
cv2.ellipse(img,center,axesLength,75,startAngle,endAngle,(0,0,255))
cv2.ellipse(img,center,axesLength,90,startAngle,endAngle,color)
cv2.ellipse(img,center,axesLength,105,startAngle,endAngle,(0,0,255))
cv2.ellipse(img,center,axesLength,120,startAngle,endAngle,color)
cv2.ellipse(img,center,axesLength,135,startAngle,endAngle,(0,0,255))
cv2.ellipse(img,center,axesLength,150,startAngle,endAngle,color)
cv2.ellipse(img,center,axesLength,175,startAngle,endAngle,(0,0,255))
cv2.ellipse(img,center,axesLength,200,startAngle,endAngle,color)
cv2.ellipse(img,center,axesLength,225,startAngle,endAngle,(0,0,255))
cv2.ellipse(img,center,axesLength,250,startAngle,endAngle,color)
cv2.ellipse(img,center,axesLength,90,30,250,(0,0,255))

cv2.ellipse(img,(50,50),(50,50),0,0,360,(0,255,255)) # Equal axes length will give a circle
cv2.ellipse(img,(250,50),(30,15),0,0,360,(0,255,255))
cv2.imshow('Ellipse drawing',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

