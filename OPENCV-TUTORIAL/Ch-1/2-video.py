import cv2

cap = cv2.VideoCapture("Assets/car.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break