import cv2
import numpy as np

# Load the Haar cascade for hand detection
hand_cascade = cv2.CascadeClassifier("hand.xml")

# Load the video capture
cap = cv2.VideoCapture(0)

# Loop through the video frames
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect hands in the grayscale frame
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    # Loop through the detected hands
    for (x, y, w, h) in hands:
        # Draw a rectangle around the hand
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    # Display the frame
    cv2.imshow("Hand Detection", frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()
