import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    exit()

#필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('video', frame)

    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()