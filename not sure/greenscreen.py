import cv2
import numpy as np
# Load the replacement image

# Open the webcam
cap = cv2.VideoCapture(0)
ret , frame = cap.read()
replacement_image = frame
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the blue pixels
    lower_blue = np.array([10,10,40])
    upper_blue = np.array([255,250,250])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Use the mask to select the blue pixels in the frame
    frame[blue_mask > 0] = replacement_image[blue_mask > 0]

    # Show the result
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)

    # Press 'q' to quit
    if key == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
