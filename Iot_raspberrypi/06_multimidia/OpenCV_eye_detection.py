import cv2

#필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

img = cv2.imread('ssd.jpg')

#Cascade 알고리즘은 흑백만 가능
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#얼굴검출
faces = face_cascade.detectMultiScale(gray)

for (x, y, w, h) in faces:  #왼쪽 위의 점의 좌표, 너비, 높이
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #그릴 그림, 시작 좌표, 끝 좌표, 선의 색(BGR), 두께

    #얼굴 안에서 눈 식별
    #RoI(관심 영역, Region of Interest) 설정
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()