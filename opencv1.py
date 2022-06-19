import cv2

# 이미지 불러오기
이미지 = cv2.imread('img1.jpg')

# 크기변경
크기변경 = cv2.resize(이미지,(700,500))

# 글자넣기
cv2.putText(크기변경,'Noh Eul', (70,120),cv2.FONT_ITALIC, 3, (150,90,150),3)

# 이미지 보여주기 (제목, 이미지명)
cv2.imshow('title', 크기변경)

# 이미지 띄워놓고 대기
cv2.waitKey(0)