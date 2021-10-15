import cv2
import  numpy as np

img = cv2.imread("Assets/car.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,300))

cv2.imshow("image",img)
cv2.imshow("image resized",imgResize)

cv2.waitKey(0)