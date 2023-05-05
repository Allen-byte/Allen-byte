# coding: utf-8

# 手势识别

import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils          # 绘制

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    if success:
        img = cv.flip(img, 180)                                     # 镜像翻转
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)               # 检测手的坐标，如果存在的话
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)          # 在每一帧图像上画出坐标landmarks
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), thickness=3)
    cv.imshow('Image', img)
    cv.waitKey(1)