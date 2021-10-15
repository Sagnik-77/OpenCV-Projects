import cv2

#Our Car Image and Video
img_file = 'Assets/car1.jpg'
video = cv2.VideoCapture("Assets/video.mp4")
#Pre-trained car classifier
classifier_file = 'Assets/car_detector.xml'
#create classifier class
car_tracker = cv2.CascadeClassifier(classifier_file)

#Run till video ends
while True:
    #Read the current frame
    (read_successful,frame) = video.read()

    #Edge cases   
    if read_successful:
        #Convert video to grayscale
        grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break

    #detect cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    #display the image with car spotted
    cv2.imshow('OpenCv car video detector', frame)
    #dont autoclose (wait here in code and listen for a key press)
    cv2.waitKey(1)

# #create opencv image
# img = cv2.imread(img_file)
# #convert classifier to grayscale(required for haar cascade)
# img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #create classifier class
# car_tracker = cv2.CascadeClassifier(classifier_file)
# #detect cars
# cars = car_tracker.detectMultiScale(img_bw)

# #detect cars and draw rectangle
# for(x,y,w,h) in cars:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


# #display the image with car spotted
# cv2.imshow('OpenCv car detector',img)
# #dont autoclose (wait here in code and listen for a key press)
# cv2.waitKey()

print('code completed')