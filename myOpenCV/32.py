# More on Mouse events

import cv2
import numpy as np

points=[]


def on_click(event,x,y,flags,param):

    # For drawing a circle
    if event==cv2.EVENT_RBUTTONDOWN:
        print("Right clicked at :",x,y)
        cv2.circle(img,(x,y),6,(0,0,255),2)
        cv2.imshow("Right click",img)
        points.append((x,y))

    # for drawing line between two latest points
    if len(points)>=2:
        cv2.line(img,points[-1],points[-2],(0,255,0),1)
        cv2.imshow('Right click',img)

    cv2.imshow('Right click',img)


img=np.zeros((512,512,3),np.uint8)
cv2.imshow('Right click',img)

cv2.setMouseCallback('Right click',on_click)

cv2.waitKey(0)
cv2.destroyAllWindows()