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
    h,w,_=img.shape
    imgColor, mask=myColorFinder.update(img,hsvVals)
    imgContour,contours=cvzone.findContours(img,mask)

    if contours:
        data=contours[0]['center'][0],\
             h-contours[0]['center'][1],\
             int(contours[0]['area'])
        print(data)

    imgStack=cvzone.stackImages([img,imgColor,mask,imgContour],2,0.5)
    cv2.imshow("Image",imgStack)

    cv2.waitKey(1)
    