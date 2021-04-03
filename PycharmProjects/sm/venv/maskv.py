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

cap=cv2.VideoCapture(0);
#tracker=cv2.legacy_TrackerMOSSE.create()
tracker=cv2.legacy_TrackerCSRT.create()
T,img=cap.read()
bbox=cv2.selectROI('tracker',img,False)
tracker.init(img,bbox)
def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, 'tracking', (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
while True:
    timer = cv2.getTickCount()
    T,img=cap.read()
    T,bbox=tracker.update(img)
    if T:
        drawbox(img,bbox)
    else:
        cv2.putText(img,'lost',(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7, (255,0,0),2)

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img=cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7, (255,0,0),2)
    cv2.imshow('image', img)


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


    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()