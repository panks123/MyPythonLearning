# Image rotation 2

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original image',img)

(width,height)=img.shape[:2]

for i in range(4):
    rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,1)
    img=cv2.warpAffine(img,rotation_matrix,(width,height))
    win=f"Rotation {i+1} -(90 deg)"
    i=i+1
    cv2.imshow(win,img)

cv2.waitKey(0)
cv2.destroyAllWindows()