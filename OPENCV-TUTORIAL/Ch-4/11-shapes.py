import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.rectangle(img,(0,0),(300,300),(0,0,255),2)
cv2.rectangle(img,(0,0),(300,300),(255,0,0),cv2.FILLED)

cv2.imshow("Matrix",img)

cv2.waitKey(0)