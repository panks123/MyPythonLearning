# cv2.cvtColor()

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original Image',img)
print(img.shape)

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',rgb)
print(rgb.shape)


hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)
print(hsv.shape)


hls=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow('HLS',hls)
print(hls.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
