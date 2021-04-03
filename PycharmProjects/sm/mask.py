import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow('tracking')
cv2.createTrackbar('l_h','tracking',0,255,nothing)
cv2.createTrackbar('l_s','tracking',0,255,nothing)
cv2.createTrackbar('l_v','tracking',0,255,nothing)
cv2.createTrackbar('u_h','tracking',255,255,nothing)
cv2.createTrackbar('u_s','tracking',255,255,nothing)
cv2.createTrackbar('u_v','tracking',255,255,nothing)
while True:
    img=cv2.imread('sm.jpg')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


    l_h=cv2.getTrackbarPos('l_h','tracking')
    l_s= cv2.getTrackbarPos('l_s', 'tracking')
    l_v= cv2.getTrackbarPos('l_v', 'tracking')

    u_h=cv2.getTrackbarPos('u_h','tracking')
    u_s = cv2.getTrackbarPos('u_s', 'tracking')
    u_v = cv2.getTrackbarPos('u_v', 'tracking')

    l_b=np.array([l_h,l_s,l_v])
    u_b = np.array([u_h, u_s, u_v])


    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_or(img,img,mask=mask)

    cv2.imshow('image',img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()