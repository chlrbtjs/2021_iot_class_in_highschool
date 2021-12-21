import cv2

cap = cv2.VideoCapture(0) #촬영시에는 0, 영상 열때는 영상 이름

if not cap.isOpened():
    print('camera open failed')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Edge = cv2.Canny(frame, 0, 100)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('Edge', Edge)

    if cv2.waitKey(10) == 13:
        break

cap.release()
out.release()
cv2.destroyALLWindows()
