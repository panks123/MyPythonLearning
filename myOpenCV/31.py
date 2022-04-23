# Mouse click events

import cv2
import numpy as np
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events) # It will print all the possible mouse events

# defining a function which will perform task when some mouse event occurs in the associated window


def click_event(event,x,y,flags,param):
    '''
    Here
    event : the openCV mouse event that is detected
    x, y :co-ordinates of the position where the event occurs:
    flags: one of the flag event of openCV
    param: optional user defined data that can be passed to the callback. Needs to be defined when registering the
    callback if we want to use it
    '''
    if event ==cv2.EVENT_LBUTTONDOWN:
        print(f'Left clicked at : ({x},{y})')

        # to put font at that position
        font =cv2.FONT_HERSHEY_SIMPLEX
        str_xy='('+str(x)+','+str(y)+')'
        cv2.putText(img,str_xy,(x,y),font,.4,(255,255,0),thickness=None)
        cv2.imshow('Image',img)

    if event == cv2.EVENT_LBUTTONDBLCLK:

        # draw a circle of radius 10
        print(f'Left double clicked at : ({x},{y})')
        cv2.circle(img,(x,y),10,(0,255,255),thickness=None)
        cv2.imshow('Image',img)


img=np.zeros((512,512,3),np.uint8)
cv2.imshow('Image',img)
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()




