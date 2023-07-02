# pip install mediapipe

import cv2
import numpy as np

# Load the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the yellow color
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Threshold the frame to get only the yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find the contours in the masked frame
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # Get the moments of the contour
        moments = cv2.moments(contour)

        # Check if the moments are valid
        if moments["m00"] != 0:
            # Get the center of the contour
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])

            # Draw a circle at the center of the contour
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            # Get the convex hull of the contour
            hull = cv2.convexHull(contour)

            # Draw the convex hull on the frame
            cv2.drawContours(frame, [hull], 0, (0, 255, 0), 2)

            # Get the defect points of the convex hull
            defects = cv2.convexityDefects(contour, hull)

            # Check if the defect points are valid
            if defects is not None:
                # Get the number of fingers by counting the defect points
                fingers = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(contour[s][0])
                    end = tuple(contour[e][0])
                    far = tuple(contour[f][0])

                    # Compute the distance between the start and end points
                    a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

                    # Check if the triangle formed by the start, end, and far points is a finger
                    if a > 0 and b > 0 and c > 0:
                        angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
                        if angle <= np.pi / 2:
                            fingers += 1

                # Display the number of fingers on the frame
                cv2.putText(frame, str(fingers), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Finger Detection", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()

# Path: fintest4.py
