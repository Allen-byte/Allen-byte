# coding: utf-8

import cv2 as cv
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    flag, img = cap.read()
    if flag:
        img = cv.flip(img, 180)
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]
        pointLeft, pointRight = face[145], face[374]             # 左右眼睛的坐标
        # cv.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv.circle(img, pointLeft, 5, (255, 0, 255), cv.FILLED)
        # cv.circle(img, pointRight, 5, (255, 0, 255), cv.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3
        f = 720                    # 摄像头焦距
        d = (W * f) / w
        if int(d) < 40:
            cvzone.putTextRect(img, f'Too close!!!', (face[10][0]-120, face[10][1]-50), scale=2)
        else:
            cvzone.putTextRect(img, f'Depth: {round(d, 2)}cm', (face[10][0] - 120, face[10][1] - 50), scale=2)
        # print(round(d, 2))
    cv.imshow('Image', img)
    key_pressed = cv.waitKey(1)
    if key_pressed == ord('q'):
        break