# Image cropping

import cv2

img=cv2.imread('lena.jpg')

(width,height)=img.shape[:2]

# co-ordinates of the cropping rectangle(top-left)

(top,left)=int(height*0.33),int(width*0.33)
print(top,left)
# co-ordinates of the cropping rectangle(bottom-right)

(bottom,right)=int(height*0.8),int(width*0.9)
print(bottom,right)

cropped=img[left:right,top:bottom]

cv2.imshow('Original',img)
cv2.imshow('cropped',cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
