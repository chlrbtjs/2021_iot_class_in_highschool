import cv2

cap = cv2.VideoCapture('output.avi') #촬영시에는 0, 영상 열때는 영상 이름

if not cap.isOpened():
    print('camera open failed')
    exit()

# ret, frame = cap.read()
# cv2.imshow('a', frame)

#four character code
#DIVX(avi로 만들때) MP4V(mp4로 만들때) X264(h264로 만들때)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D', 'I', 'V', 'X') 로 해도 됨
#out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480)) #(이름, fourcc, fps, size)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    #out.write(frame)

    if cv2.waitKey(10) == 13:
        break

# while True:
#     if cv2.waitKey() == 13:
#         break

#cv2.imwrite('camera.jpg', frame)

cap.release()
out.release()
cv2.destroyALLWindows()
