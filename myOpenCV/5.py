
import cv2
img=cv2.imread('lenaModified.png')

print(type(img)) # So it is actually a numpy array

# So we can use any numpy array operations
print(img.shape) # It returns a tuple containing no. of pixels in height, width of the image and
                    # the no. of layers of the image here it is 3(for RGB)
print(img.ndim)