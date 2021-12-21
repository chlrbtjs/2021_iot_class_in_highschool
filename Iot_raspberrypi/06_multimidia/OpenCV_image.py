import cv2

img = cv2.imread('ssd.jpg')
img2 = cv2.resize(img, (1000, 800))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Edge 선 추출
Edge1 = cv2.Canny(img, 0, 100)
Edge2 = cv2.Canny(img, 100, 150)
Edge3 = cv2.Canny(img, 150, 200)

#cv2.imshow('a', img)
#cv2.imshow('b', img2)
#cv2.imshow('c', gray)

cv2.imshow('d', Edge1)
cv2.imshow('e', Edge2)
cv2.imshow('f', Edge3)

# A : 65 a : 97 ENTER : 13 ESC : 27
while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('ssd_gray.jpg', gray)

cv2.destroyALLWindows()