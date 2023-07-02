# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Define range of yellow color in HSV
#     lower_yellow = np.array([20, 100, 100])
#     upper_yellow = np.array([30, 255, 255])

#     # Threshold the HSV image to get only yellow colors
#     mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

#     # Find contours in the mask
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Loop through all contours
#     for contour in contours:
#         # Get convex hull of the contour
#         hull = cv2.convexHull(contour)

#         # Get the number of corners in the convex hull
#         corners = cv2.cornerHarris(hull, 2, 3, 0.04)

#         # Get the number of fingers by counting the number of corners
#         num_fingers = np.sum(corners > 0.01)

#         # Draw the contour on the frame
#         cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)

#         # Write the number of fingers on the frame
#         cv2.putText(frame, "Fingers: " + str(num_fingers), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     # Show the result
#     cv2.imshow("Result", frame)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    res = cv2.bitwise_and(frame, frame, mask=mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    dst = cv2.cornerHarris(gray, 1, 2, 0.01)
    # q: what does this do?
    # a: it detects the corners of the hand and draws a red circle around them
    # q: what is 0.04?
    # a: it is the threshold for the corner detection
    # q: what is 2?
    # a: it is the aperture parameter for the Sobel operator
    # q: what is 3?
    # a: it is the aperture parameter for the Sobel operator


    frame[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# what deos this do?
# a: it detects the corners of the hand and draws a red circle around them
