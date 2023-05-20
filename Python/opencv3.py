
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

#print('cv2 완료')
# 터미널창에 pip install opencv-python
# 터미널창에 pip install python-opencv
# pip install pyinstaller
# pyinstaller -w -F --icon="myico.ico" "opencv3.py"
# pyinstaller -w -F "파일명.py"

def hangulText(image, text, pos, size, color):
    img_pil = Image.fromarray(image)       # 이미지를 np리스트형태로 만든다
    img_draw = ImageDraw.Draw(img_pil)          # 그림을 그릴 공간 지정
    font = ImageFont.truetype('MALGUN.TTF', size)       # 폰트와 사이즈 설정
    img_draw.text(pos, text, font=font, fill=color)     # 글자 그리기
    return np.array(img_pil)


width = 220
height = 300

origin_pos = np.array([ [180, 130], [270, 130], [180, 255], [270, 255] ], dtype=np.float32)
change_pos = np.array([ [0, 0], [width,0], [0, height], [width, height] ], dtype=np.float32)
matrix = cv2.getPerspectiveTransform(origin_pos, change_pos)

img = cv2.imread('lemon.jpg')        # 이미지 읽기
img_change = cv2.warpPerspective(img, matrix, (width, height))

img_change = hangulText(img_change, '노을', (10, 10), 30, (255, 0, 255))

cv2.imshow('my title', img)                 # 원본 이미지 보여주기
cv2.imshow('change image', img_change)      # 자른 이미지 보여주기
cv2.waitKey(0)                          # 무한대기


# 180, 130  왼쪽위
# 270, 130  오른쪽위
# 180, 255  왼쪽아래
# 270, 255  오른쪽아래