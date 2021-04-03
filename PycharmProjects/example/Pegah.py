import cv2

def empty(a):
    pass
cv2.namedWindow("trackedbar")
cv2.resizeWindow("trackedbar",300,200)

cv2.createTrackbar("Hue Minimum","trackedbar",0,179,empty)
cv2.createTrackbar("Hue Maximum","trackedbar",179,179,empty)
cv2.createTrackbar("Sat Minimum","trackedbar",0,255,empty)
cv2.createTrackbar("Sat Maximum","trackedbar",255,255,empty)
cv2.createTrackbar("Value Minimum","trackedbar",0,255,empty)
cv2.createTrackbar("Value Maximum","trackedbar",255,255,empty)

img=cv2.imread('lena.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('lena',img)
cv2.imshow('lena.converted',img1)

cv2.waitKey(0)
