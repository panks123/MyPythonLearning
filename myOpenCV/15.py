# Adding border (extra padding) to the image

# copyMakeBorder()is used to set the borders
# cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)

# src: It is the source image.
# top: It is the border width in number of pixels in top direction.
# bottom: It is the border width in number of pixels in bottom direction.
# left: It is the border width in number of pixels in left direction.
# right: It is the border width in number of pixels in right direction.
# borderType: It depicts what kind of border to be added. It is defined by flags like
# cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc
# value: is optional parameter which specifies the color of the border when borderType is cv2.BORDER_CONSTANT

import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('Original image',img)

# cv2.BORDER_CONSTANT: It adds a constant colored border. The value should be given as next argument.
img1=cv2.copyMakeBorder(img,10,5,7,8,cv2.BORDER_CONSTANT,0)
cv2.imshow('cv2.BORDER_CONSTANT',img1)

# cv2.BORDER_REFLECT: The border will be mirror reflection of the border elements.
img2=cv2.copyMakeBorder(img,1,100,50,50,cv2.BORDER_REFLECT)
cv2.imshow('cv2.BORDER_REFLECT',img2)

# cv2.BORDER_REPLICATE: It replicates the last element.
img3=cv2.copyMakeBorder(img,100,100,50,50,cv2.BORDER_REPLICATE)
cv2.imshow('cv2.BORDER_REPLICATE',img3)


cv2.waitKey(0)
cv2.destroyAllWindows()