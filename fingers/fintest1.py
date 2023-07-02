import cv2
import numpy as np

# Define the background subtraction method (Codebook Model in this case)
fgbg = cv2.createBackgroundSubtractorMOG2()

# Start capturing frames from the webcam
cap = cv2.VideoCapture(0)

lower_yellow = (0, 100, 40)
upper_yellow = (45, 250, 250)
while True:
    # Read the current frame
    ret, frame = cap.read()
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define a mask for the yellow color range
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Apply the mask to the frame to obtain only the yellow region
    yellow_region = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Apply background subtraction on the yellow region
    fgmask = fgbg.apply(yellow_region)
    
    # Threshold the foreground mask to obtain a binary image
    thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)[1]
    
    # Perform morphological operations to clean up the binary image
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter the contours to only keep the contours that represent fingers
    fingers = []
    for c in contours:
        if cv2.contourArea(c) > 100:
            (x, y, w, h) = cv2.boundingRect(c)
            if mask[y:y+h, x:x+w].sum() == h*w:
                fingers.append(c)
    
    # Draw the filtered contours on the original image
    for finger in fingers:
        (x, y, w, h) = cv2.boundingRect(finger)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    
    # Display the original image with the detected fingers and the count
    cv2.putText(frame, "Fingers: " + str(len(fingers)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow("Finger Detection", yellow_region)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


