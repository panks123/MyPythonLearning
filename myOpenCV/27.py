# Canny edge detection

# The canny edge detection algorithm is a multi stage algorithm that includes:
# 1. Noise Reduction
# 2. Finding Intensity Gradient of the Image
# 3. Non-maximum Suppression
# 4. Double threshold
# 5. Hysteresis Thresholding - edge tracking by hysteresis


import cv2

img=cv2.imread('lena.jpg',0)

canny=cv2.Canny(img,100,200)  # here 100 is threshold 1 and 200 is the threshold 2

cv2.imshow('Original',img)
cv2.imshow('Canny',canny)
print(canny)

cv2.waitKey(0)
cv2.destroyAllWindows()



