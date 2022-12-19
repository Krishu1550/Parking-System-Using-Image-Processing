import cv2 as cv
import numpy as np
import cvzone
import pickle
width,height=105,45

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def checkParkingSpace(image):
    spaceCounter = 0
    for pos in posList:
        x,y=pos
        cropimg= image[y:y+height,x:x+width]
        #cv.imshow(str(x*y),cropimg)
        count = cv.countNonZero(cropimg)
        if count < 500:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(frame,str(count),(x,y+height-10),scale=0.8,thickness=2)

        cvzone.putTextRect(frame, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0, 200, 0))

cap= cv.VideoCapture("Resource/carPark.mp4")
while cap.isOpened():
    sucess, frame= cap.read()
    imggray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    imgblur= cv.GaussianBlur(imggray,(3,3),1)
    binaryImg=cv.adaptiveThreshold(imgblur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv.THRESH_BINARY_INV,25,16)
    imgmedian=cv.medianBlur(binaryImg,5)
    checkParkingSpace(imgmedian)

    cv.imshow("Frame",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
