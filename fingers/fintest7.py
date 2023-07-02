import numpy as np
import cv2

def distance(point_1, point_2):
  return np.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def get_finger_distance(frame):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5,5), 0)
  thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
  contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  max_contour = max(contours, key = cv2.contourArea)
  
  if len(max_contour) >= 3:
    convex_hull = cv2.convexHull(max_contour)
    defects = cv2.convexityDefects(max_contour, convex_hull)
  else:
    defects = None
  
  if defects is not None:
    far_points = []
    for i in range(defects.shape[0]):
      s, e, f, d = defects[i, 0]
      start = tuple(max_contour[s][0])
      end = tuple(max_contour[e][0])
      far = tuple(max_contour[f][0])
      far_points.append(far)
    if len(far_points) >= 2:
      finger_1, finger_2 = far_points[:2]
      return distance(finger_1, finger_2)
  return 0

cap = cv2.VideoCapture(0)
while True:
  ret, frame = cap.read()
  finger_distance = get_finger_distance(frame)
  cv2.putText(frame, "Finger Distance: {:.2f}".format(finger_distance), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
  cv2.imshow("Frame", frame)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break
cap.release()
cv2.destroyAllWindows()
