import cv2 as cv
import pickle


width,height=105,45
postion=[]

def mouseClick(events,x,y,flags,params):

    if events == cv.EVENT_LBUTTONDOWN:
        postion.append((x,y))
    if events == cv.EVENT_RBUTTONDOWN:
        print("helloR")
        for i,pos in enumerate(postion):
            x1,y1=pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                postion.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(postion, f)

while True:
    img = cv.imread("Resource/carParkImg.png")
    #cv.rectangle(img,(50,100),(200,150),(255,0,255),2)

    for pos in postion:
        cv.rectangle(img, pos, (pos[0]+width,pos[1]+height), (255, 0, 255), 2)
    cv.imshow("img", img)
    cv.setMouseCallback("img", mouseClick)

    cv.waitKey(1)
