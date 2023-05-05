# coding: utf-8

import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture("./sources/01.mp4")
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

pTime = 0

while True:
    flag, img = cap.read()
    if flag:
        img = cv.flip(img, 180)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        # for id, lm in enumerate(results.pose_landmarks.landmark):
        #     h, w, c = img.shape
        #     cx, cy = int(lm.x * w), int(lm.y * h)
        #     cv.circle(img, (cx, cy), 5, (123, 34, 56), cv.FILLED)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), thickness=3)
    cv.imshow('Image', img)
    cv.waitKey(1)