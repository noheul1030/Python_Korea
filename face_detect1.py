import cv2                  #pip install opencv-python
import mediapipe as mp      #pip install mediapipe

# 이미지에서 얼굴찾기
cap = cv2.VideoCapture('어린이.jpg')

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.60)     # 60% 이상 얼굴로 인식될경우

success, img = cap.read()
if success :
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection)        # 얼굴 위치에에 네모 표시
    cv2.imshow('Image',img)
    cv2.waitKey(0)