# Drawing text

# cv2.putText() method is used
# Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
#
# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.
# org: It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are
# represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.

import cv2
import numpy as np

img=np.zeros((312,312,3),np.uint8)

text='Pankaj'
org=(150,150)
font=cv2.FONT_HERSHEY_SIMPLEX
fontScale=1
cv2.putText(img,text,org,font,fontScale,(0,255,255))
cv2.putText(img,"Kumar",(30,100),cv2.FONT_HERSHEY_COMPLEX,fontScale,(0,255,0))
cv2.putText(img,"Renu",(160,90),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.5,(255,0,255))
cv2.putText(img,"Kumari",(120,190),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.2,(0,0,255))

cv2.imshow('Text drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()