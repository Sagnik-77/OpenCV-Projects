import cv2

img = cv2.imread("Assets/intro.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage",imgGray)
cv2.waitKey(0)