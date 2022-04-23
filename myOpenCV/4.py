# Writing a file

# cv2.imwrite() method is used to save an image to any storage device.
# This will save the image according to the specified format in current working directory.

# Syntax: cv2.imwrite(filename, image)

import cv2
img=cv2.imread('lena.jpg')

cv2.imshow('Image',img)

cv2.waitKey(0)


print(img)

for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(1):
            img[i][j][k]=0

print("_____________________________________________")
print(img)

cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the modified image

cv2.imwrite('lenaModified.jpg',img)
cv2.imwrite('lenaModified.png',img)
