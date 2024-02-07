import cvzone
from cvzone.ColorModule import ColorFinder 
import cv2
import socket

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# ColorFinder aracını aktive etme
myColorFinder=ColorFinder(False)
hsvVals = {'hmin': 23, 'smin': 67, 'vmin': 151, 'hmax': 30, 'smax': 255, 'vmax': 255}
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddressPort=("127.0.0.1",5052)


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
        sock.sendto(str.encode(str(data)),serverAddressPort)

        
    imgStack=cvzone.stackImages([img,imgColor,mask,imgContour],2,0.5)
    cv2.imshow("Image",imgStack)

    cv2.waitKey(1)
    