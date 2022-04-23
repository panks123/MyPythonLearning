# Image rotation - Rotating the image by an angle

import cv2

img=cv2.imread('lena.jpg')
(width,height)=img.shape[:2]
# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 60 degree without scaling.

rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),60,1)

rotated=cv2.warpAffine(img,rotation_matrix,(width,height))

cv2.imshow('Original',img)
cv2.imshow('Rotated without scaling',rotated)

# We want matrix for rotation w.r.t center to 60 degree with scaling (0.5).

rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),60,0.5)

rotated1=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow('Rotated with scaling(0.5)',rotated1)

# We want matrix for rotation w.r.t center to 60 degree with scaling (0.8).
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),60,0.8)

rotated2=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow('Rotated with scaling(2)',rotated2)
cv2.waitKey(0)
cv2.destroyAllWindows()



