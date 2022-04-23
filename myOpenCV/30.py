# Image blending app (Not working)
# Image blending means adding images with transparency
import cv2


def nothing(x):
    pass


img1=cv2.imread('lena.jpg')
img2=cv2.imread('girl.jpg')

# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)

output=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('ble',img2)


cv2.namedWindow('Blend app')
cv2.createTrackbar('Alpah','Blend app',0,10000,nothing)

while True:
    cv2.imshow('Blend app',output)

    if cv2.waitKey(1)==27:
        break

    alpha=cv2.getTrackbarPos('Alpha','Blend app')/10000

    beta=1-alpha

    output=cv2.addWeighted(img1,alpha,img2,beta,0)
    print(alpha,beta)

cv2.destroyAllWindows()
