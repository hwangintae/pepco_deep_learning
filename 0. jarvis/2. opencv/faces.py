import cv2
 
faceCascPath ="c:/Users/int/Anaconda3/envs/dl/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyeCascPath ="c:/Users/int/Anaconda3/envs/dl/Lib/site-packages/cv2/data/haarcascade_eye.xml"
 
faceCascade = cv2.CascadeClassifier(faceCascPath)
eye_cascade = cv2.CascadeClassifier(eyeCascPath)
 
video_capture = cv2.VideoCapture(0)
 
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
    )
 
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
                xcordEnd = x + w
        ycordEnd = y + h
        color = (255, 0, 0)
        stroke = 2
        cv2.rectangle(frame, (x, y), (xcordEnd, ycordEnd), color, stroke)
        
        # eye
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        imgItem = "myImage.png"
        cv2.imwrite(imgItem, roi_gray)
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
 
    # Display the resulting frame
    frame = cv2.flip(frame, 1)
    cv2.imshow('Video', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # When everything is done, release the capture
        video_capture.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        break
