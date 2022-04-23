# Adding trackbar to the image window

# There are times when you want to run the program with different value or parameter and experiment
# to find the optimum value to figure out the best parameter value. Editing the variable value in source code
# and running the program, again and again, can be tedious, instead, you can bind trackbars to the output image window.

# These trackbars will either call a function or update variable value based on slider position
# Trackbar is a GUI element that let the user to select a specific value within a range of values
# by sliding a slider linearly
# To create a trackbar in OpenCV  cv2.createTrackbar() function is used and to read the current poisition
# of the trackbar slider cv2.getTrackbarPos() is used and to change the position of trackbar use cv2.setTrackbarPos().

# cv2.createTrackbar() arguments
# 1. Trackbar name
# 2. Window name
# 3. Default slider value
# 4. Maximum value
# 5. Callback function

# cv2.getTrackbarPos() arguments
# 1. Trackbar name
# 2. Window name

# cv2.setTrackbarPos() arguments
# 1. Trackbar name
# 2. Window name
# 3. New Value

import cv2
import numpy as np

# Define a function which can be used as call back function for the trackbar


def nothing(x):
    pass


# create a separate window named 'controls' for trackbar
cv2.namedWindow('img')
# creating a Switch trackbar
cv2.createTrackbar('Switch','img',0,1,nothing)
# Creating a trackbar for variable radius
cv2.createTrackbar('Radius','img',15,255,nothing)

# create a while loop act as refresh for the view
while True:

    # Creating a black image
    img=np.zeros((512,512,3),np.uint8)

    # Calculating center of image
    x_center=img.shape[0]//2
    y_center=img.shape[1]//2
    switch=cv2.getTrackbarPos('Switch','img')
    if switch==0:
        cv2.circle(img, (x_center, y_center), 10, (0, 0, 255), -1)
    else:
        radius = int(cv2.getTrackbarPos('Radius', 'img'))
        # draw a red circle in the center of the image with radius set by trackbar position
        cv2.circle(img, (x_center, y_center), radius, (0, 0, 255), -1)

    cv2.imshow('img',img)

    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


