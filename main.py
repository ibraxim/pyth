import cvzone
from cvzone.ColorModule import ColorFinder 
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# ColorFinder aracını aktive etme
myColorFinder=ColorFinder(False)
hsvVals = {'hmin': 23, 'smin': 67, 'vmin': 151, 'hmax': 30, 'smax': 255, 'vmax': 255}

while True:
    success,img =cap.read()
    imgColor, mask=myColorFinder.update(img,hsvVals)

    imgStack=cvzone.stackImages([img,imgColor,mask],2,0.5)
    cv2.imshow("Image",imgStack)

    cv2.waitKey(1)
    