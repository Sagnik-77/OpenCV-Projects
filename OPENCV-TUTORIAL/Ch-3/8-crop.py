import cv2
import  numpy as np

img = cv2.imread("Assets/car.jpg")

imgCropped = img[0:600,200:500]

cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)