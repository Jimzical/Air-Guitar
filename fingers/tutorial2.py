# for saved image
# custom code

# import cv2
# import mediapipe as mp

# cap = cv2.VideoCapture(0)
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils

# print(mpHands)
# while True:
#     success, image = cap.read()
#     imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(imageRGB)


#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks: # working with each hand
#             for id, lm in enumerate(handLms.landmark):
#                 h, w, c = image.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#     if id == 20 :
#         cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

#     mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

#     cv2.imshow("Image",cv2.flip(image, 1))

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


image = cv2.imread("image.jpg")

image = cv2.flip(image, 1)

imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = hands.process(imageRGB)

# print(results.multi_hand_landmarks[0].landmark[0])

point = {"Wrist" : results.multi_hand_landmarks[0].landmark[0], "Thumb MCP" : results.multi_hand_landmarks[0].landmark[1], "Thumb IP" : results.multi_hand_landmarks[0].landmark[2], "Thumb Tip" : results.multi_hand_landmarks[0].landmark[3], "Index MCP" : results.multi_hand_landmarks[0].landmark[4], "Index PIP" : results.multi_hand_landmarks[0].landmark[5], "Index DIP" : results.multi_hand_landmarks[0].landmark[6], "Index Tip" : results.multi_hand_landmarks[0].landmark[7], "Middle MCP" : results.multi_hand_landmarks[0].landmark[8], "Middle PIP" : results.multi_hand_landmarks[0].landmark[9], "Middle DIP" : results.multi_hand_landmarks[0].landmark[10], "Middle Tip" : results.multi_hand_landmarks[0].landmark[11], "Ring MCP" : results.multi_hand_landmarks[0].landmark[12], "Ring PIP" : results.multi_hand_landmarks[0].landmark[13], "Ring DIP" : results.multi_hand_landmarks[0].landmark[14], "Ring Tip" : results.multi_hand_landmarks[0].landmark[15], "Pinky MCP" : results.multi_hand_landmarks[0].landmark[16], "Pinky PIP" : results.multi_hand_landmarks[0].landmark[17], "Pinky DIP" : results.multi_hand_landmarks[0].landmark[18], "Pinky Tip" : results.multi_hand_landmarks[0].landmark[19], "Palm Center" : results.multi_hand_landmarks[0].landmark[20]}


print(point["Wrist"].x, point["Wrist"].y, point["Wrist"].z)

# for handLms in results.multi_hand_landmarks: # working with each hand
#     # print(handLms.landmark[0].x)
#     # print(handLms.landmark[0].y)
#     # print(handLms.landmark[0].z)

#     for id, lm in enumerate(handLms.landmark):
#         # print("id: ", id, "\nx: ", lm.x, "\|ny: ", lm.y, "\nz: ", lm.z)
#         h, w, c = image.shape
#         cx, cy = int(lm.x * w), int(lm.y * h)

#         if id <= 20 :
#             cv2.putText(image, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, lm.z * -10, (0, 250, 0), 2)

#     mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

# cv2.imshow("Image",image)
# cv2.waitKey(0)


