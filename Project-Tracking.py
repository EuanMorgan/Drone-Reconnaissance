import cv2
import numpy as np


def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.2,8)

    faceListC = []
    faceListArea = []
    #draw rectangle around face, draw circle at center
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x+w//2
        cy = y+h//2
        area = w*h
        cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
        faceListC.append([cx,cy])
        faceListArea.append(area)
    if len(faceListArea) != 0:
        #find max value of area i.e. closest face
        #closer the face = higher area, based on this move the drone
        i = faceListArea.index(max(faceListArea))
        return img, [faceListC[i],faceListArea[i]]
    else:
        return img, [[0,0],0]
cap = cv2.VideoCapture(0)

while True:
    #get new img from webcam, pass to find face
    _,img = cap.read()
    img, info = findFace(img)
    print("Area",  info[1])
    cv2.imshow("Cam", img)
    cv2.waitKey(1)