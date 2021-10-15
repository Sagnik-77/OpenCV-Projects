import cv2

img = cv2.imread("Assets/intro.png")
imgCanny = cv2.Canny(img,100,100)

cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)