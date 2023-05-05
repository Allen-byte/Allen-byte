# coding: utf-8

import cv2 as cv
import time
import mediapipe as mp

cap = cv.VideoCapture(0)
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
pTime = 0
index = 1

while True:
    flag, img = cap.read()
    if flag:
        img = cv.flip(img, 180)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, "FPS: " + str(int(fps)), (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), thickness=3)
    cv.imshow('Image', img)
    key_pressed = cv.waitKey(1)
    if key_pressed == ord('s'):
        cv.imwrite(f'./sources/face_{index}.jpg', img)
        print("已保存")
        index += 1