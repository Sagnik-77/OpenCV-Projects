import cv2

img = cv2.imread("Assets/intro.png")
imgBlur = cv2.GaussianBlur(img,(7,7),0)

cv2.imshow("GrayImage",imgBlur)
cv2.waitKey(0)