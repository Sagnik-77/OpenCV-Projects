import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img[:]=255,0,0

cv2.imshow("Matrix",img)

cv2.waitKey(0)