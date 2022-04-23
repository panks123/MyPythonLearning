# Image Sharpening

# Applying the sharpening filter will sharpen the edges in the image. This filter is very useful when we want
# to enhance the edges in an image that's not crisp.
# level of sharpening depends on the type of kernel we use. We can customize our kernel and each kernel will
# give different kind of sharpening
# To sharpen an image we will use a kernel like [[-1,-1,-1]
#                                                [-1,9,-1]
#                                                [-1,-1,-1]]

import cv2
import  numpy as np

img=cv2.imread('ex.jpg')
# img=cv2.imread('ex1.jpg')
# img=cv2.imread('ex2.jpg')

cv2.imshow('Original',img)

kernel1=np.array([[-1,-1,-1],
                  [-1,9,-1],
                  [-1,-1,-1]])

# Sharpening

output1=cv2.filter2D(img,-1,kernel1)
cv2.imshow('Sharpening',output1)

# If we want to do excessive sharpening, like in the bottom left image, we would use
# the following kernel:

kernel2=np.array([[1,1,1],
                  [1,-7,1],
                  [1,1,1]])

output2=cv2.filter2D(img,-1,kernel2)
cv2.imshow('Excessive sharpening',output2)

# But the problem with these two kernels is that the output image looks artificially
# enhanced. If we want our images to look more natural, we would use an Edge
# Enhancement filter. The underlying concept remains the same, but we use an
# approximate Gaussian kernel to build this filter. It will help us smoothening of the image
# when we enhance the edges, thus making the image look more natural.

kernel3=np.array([ [-1,-1,-1,-1,-1],
                    [-1,2,2,2,-1],
                    [-1,2,8,2,-1],
                    [-1,2,2,2,-1],
                    [-1,-1,-1,-1,-1] ]) / 8.0

output3=cv2.filter2D(img,-1,kernel3)
cv2.imshow('Edge enhancement',output3)

cv2.waitKey(0)
cv2.destroyAllWindows()
