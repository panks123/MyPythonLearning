# Reading an image

import cv2

img=cv2.imread('lena.jpg') # To read the images cv2.imread() method is used.
                           # It reads the image in the Form of a matrix based on the number of color channels present

print(img)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array

cv2.imshow('Lena',img)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 is passed , then it will
# hold the screen until user close it.
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()