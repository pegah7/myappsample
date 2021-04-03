import cv2

import time
cap=cv2.VideoCapture(0)


while True:
    success,img=cap.read()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("image",img)
    cv2.waitKey(1)