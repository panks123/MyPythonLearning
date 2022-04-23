# Image translation

# Translation refers to the rectilinear shift of an object i.e. an image from one location to another. If we know the
# amount of shift in horizontal and the vertical direction, say (tx, ty) then we can make a transformation matrix
# e.g. [[1,0,tx],
#       [0,1,ty]]
# where tx denotes the shift along the x-axis and ty denotes shift along the y-axis i.e. the number of pixels by which
# we need to shift about in that direction.

# we use cv2.wrapAffine() function to implement these translations, This function requires a 2×3 array.
# The numpy array should be of float type.

import cv2
import numpy as np

img=cv2.imread('lena.jpg')
cv2.imshow('Original',img)

width,height=img.shape[:2]

quarter_ht,quarter_wd=height/4,width/4

T = np.float32([[1, 0, quarter_wd], [0, 1, quarter_ht]])

translated1=cv2.warpAffine(img,T,(width,height))
translated2=cv2.warpAffine(img,T,(width*2,height*2))

cv2.imshow('Translated1',translated1)
cv2.imshow('Translated2',translated2)
cv2.waitKey(0)
cv2.destroyAllWindows()
