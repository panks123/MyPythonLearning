# Reading an image

# Syntax: cv2.imread(path, flag)

# here flag can take three values

# 1. cv2.IMREAD_COLOR (it's numeric value is 1) -- and it is default value
# 2. cv2.IMREAD_GRAYSCALE (it's numeric value is 0)
# 3. cv2.IMREAD_UNCHANGED (it's numeric value is -1)

import  cv2

# Reading as a Gray scale image
img= cv2.imread('lena.jpg',0)
cv2.imshow('Lena- Gray',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# ------------------------------------------------------------------

img= cv2.imread('lena.jpg',-1)
cv2.imshow('Lena- UNCHANGED',img)
cv2.waitKey(0)

cv2.destroyAllWindows()