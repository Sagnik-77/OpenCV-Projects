import cv2

print('pacakge imported')
img = cv2.imread("Assets/intro.png")
cv2.imshow("output",img)
cv2.waitKey(0)