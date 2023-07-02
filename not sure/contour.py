import cv2
import numpy as np
# from testbat import ProperShow
# Initialize webcam
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to remove noise
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    # Threshold the image to binary
    ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    max_area = 0
    max_contour = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            max_contour = cnt

    # Draw the largest contour on the frame
    if max_contour is not None:
        cv2.drawContours(frame, [max_contour], 0, (0,255,0), 2)

    # Approximate the contour to a polygon
    epsilon = 0.02*cv2.arcLength(max_contour, True)
    approx = cv2.approxPolyDP(max_contour, epsilon, True)

    # Count the number of vertices in the polygon
    fingers = len(approx) - 1

    # Display the number of fingers
    cv2.putText(frame, "Fingers: {}".format(fingers), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    # Display the frame
    cv2.imshow("Webcam", frame)
    # ProperShow(frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()
