# Drawing an arrowed line

# cv2.arrowedLine() method is used
# Syntax: cv2.arrowedLine(image, start_point, end_point, color[, thickness[, line_type[, shift[, tipLength]]]])

import cv2
import numpy as np

img=np.zeros((312,312,3),np.uint8)

cv2.arrowedLine(img,(50,156),(312-50,156),(0,0,255),tipLength=0.1)  # Here tipLength parameter is the relative factor
#                                                                    to the  arrow length

cv2.arrowedLine(img,(34,78),(90,90),(0,0,255),tipLength=0.3)

cv2.imshow('Arrowed line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()