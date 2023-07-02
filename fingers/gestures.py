# google tutorial 

import cv2
import mediapipe as mp
import pyautogui as gui

def detectLandMarks(image, hands):
# TODO: Remove this function

    # Image to output
    new_image = image.copy()
 
    # Converting image to RGB
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
 
    # Check if landmarks are found
    if results.multi_hand_landmarks:
        # Iterate over the found hands
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the landmark onto the image
            mp_drawing.draw_landmarks(image = output_image, landmark_list = hand_landmarks)
 
            return output_image


def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands



    # For webcam input:
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            image =  cv2.flip(image, 1)
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)


            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:

                point = {"Wrist" : results.multi_hand_landmarks[0].landmark[0], "Thumb MCP" : results.multi_hand_landmarks[0].landmark[1], "Thumb IP" : results.multi_hand_landmarks[0].landmark[2], "Thumb Tip" : results.multi_hand_landmarks[0].landmark[3], "Index MCP" : results.multi_hand_landmarks[0].landmark[4], "Index PIP" : results.multi_hand_landmarks[0].landmark[5], "Index DIP" : results.multi_hand_landmarks[0].landmark[6], "Index Tip" : results.multi_hand_landmarks[0].landmark[7], "Middle MCP" : results.multi_hand_landmarks[0].landmark[8], "Middle PIP" : results.multi_hand_landmarks[0].landmark[9], "Middle DIP" : results.multi_hand_landmarks[0].landmark[10], "Middle Tip" : results.multi_hand_landmarks[0].landmark[11], "Ring MCP" : results.multi_hand_landmarks[0].landmark[12], "Ring PIP" : results.multi_hand_landmarks[0].landmark[13], "Ring DIP" : results.multi_hand_landmarks[0].landmark[14], "Ring Tip" : results.multi_hand_landmarks[0].landmark[15], "Pinky MCP" : results.multi_hand_landmarks[0].landmark[16], "Pinky PIP" : results.multi_hand_landmarks[0].landmark[17], "Pinky DIP" : results.multi_hand_landmarks[0].landmark[18], "Pinky Tip" : results.multi_hand_landmarks[0].landmark[19], "Palm Center" : results.multi_hand_landmarks[0].landmark[20]}

                for hand_no,hand_landmarks in enumerate(results.multi_hand_landmarks):
                    for part,vals in point.items():
                        h , w , c = image.shape
                        cx , cy = int(vals.x * w) , int(vals.y * h)
                        cv2.putText(image,"{:.2f} {:.2f}".format(vals.x,vals.y), (cx, cy), cv2.FONT_HERSHEY_PLAIN, vals.z * -5, (0, 0, 255), 1)

                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
                        
                # print(point["Index Tip"].x,point["Index Tip"].y,point["Index Tip"].z)
                # print(point["Thumb Tip"].x,point["Thumb Tip"].y,point["Thumb Tip"].z)
                print(point["Index MCP"].x - point["Thumb Tip"].x,point["Index MCP"].y - point["Thumb Tip"].y,point["Index MCP"].z - point["Thumb Tip"].z)
                Xcoord = point["Index Tip"].x * gui.size()[0]
                Ycoord = point["Index Tip"].y * gui.size()[1]

                # print(Xcoord,Ycoord)

                # move mouse
                # gui.moveTo(Xcoord,Ycoord)

                if Xcoord < 0:
                    break
                # gui.sleep(0.5)
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands',image)


            if cv2.waitKey(0) & 0xFF == 27 or cv2.waitKey(0) & 0xFF == ord("q"):
                break



            # if cv2.waitKey(5) & 0xFF == 27 or cv2.waitKey(5) & 0xFF == ord("q") or (point["Index Tip"].x - point["Thumb Tip"].x == 0.1 and point["Index Tip"].y - point["Thumb Tip"].y == 0.1):
                # break

    cap.release()


if __name__ == "__main__":
    main()