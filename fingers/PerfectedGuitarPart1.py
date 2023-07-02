# google tutorial 
# move mouse
import cv2
import mediapipe as mp
import pyautogui as gui

def move_mouse(point):
    Xcoord = point["Index Tip"].x * gui.size()[0]
    Ycoord = point["Index Tip"].y * gui.size()[1]

    print(Xcoord,Ycoord)

    # move mouse
    gui.moveTo(Xcoord,Ycoord)

    if Xcoord < 0:
        cap.release()
        exit()
        # return False

def DistanceBetweenTwoPoints(point1, point2):
    dist = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5
    # # take z vaule into account
    # dist = dist + (point1.z - point2.z)**2
    
    # normalize using z value as reference
    dist = dist / -point1.z


    return dist

def DrawLine(image,point1,point2,length = 3 ):
    # # draw line from wrist to index
    
    # startpoint = (int(point1.x * gui.size()[0] /2) ,int(point1.y * gui.size()[1] /2)) 
    # endpoint = (int(point2.x * gui.size()[0] /2) ,int(point2.y * gui.size()[1] /2) )

    startpoint = (int(point1.x * 640) ,int(point1.y * 480))
    endpoint = (int(point2.x * 640) ,int(point2.y * 480))

    endpoint = (int(endpoint[0] + (endpoint[0] - startpoint[0]) * length),int(endpoint[1] + (endpoint[1] - startpoint[1]) * length))
    cv2.line(image, startpoint, endpoint, (255,0,0), 5)

    # slope = (endpoint[1] - startpoint[1]) / (endpoint[0] - startpoint[0])
    return





def ResizeWithAspectRatio(image, width = 1920, height= 1080, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    r = width / float(w)
    dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def main():

    global cap

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
                
                point = {"Wrist" : results.multi_hand_landmarks[0].landmark[0] ,"Thumb CMC" : results.multi_hand_landmarks[0].landmark[1], "Thumb MCP" : results.multi_hand_landmarks[0].landmark[2], "Thumb IP" : results.multi_hand_landmarks[0].landmark[3], "Thumb Tip" : results.multi_hand_landmarks[0].landmark[4], "Index MCP" : results.multi_hand_landmarks[0].landmark[5], "Index PIP" : results.multi_hand_landmarks[0].landmark[6], "Index DIP" : results.multi_hand_landmarks[0].landmark[7], "Index Tip" : results.multi_hand_landmarks[0].landmark[8], "Middle MCP" : results.multi_hand_landmarks[0].landmark[9], "Middle PIP" : results.multi_hand_landmarks[0].landmark[10], "Middle DIP" : results.multi_hand_landmarks[0].landmark[11], "Middle Tip" : results.multi_hand_landmarks[0].landmark[12], "Ring MCP" : results.multi_hand_landmarks[0].landmark[13], "Ring PIP" : results.multi_hand_landmarks[0].landmark[14], "Ring DIP" : results.multi_hand_landmarks[0].landmark[15], "Ring Tip" : results.multi_hand_landmarks[0].landmark[16], "Pinky MCP" : results.multi_hand_landmarks[0].landmark[17], "Pinky PIP" : results.multi_hand_landmarks[0].landmark[18], "Pinky DIP" : results.multi_hand_landmarks[0].landmark[19], "Pinky Tip" : results.multi_hand_landmarks[0].landmark[20]}
                # cv2.line(image,(0 , 0), (int(point["Index Tip"].x * 640),int(point["Index Tip"].y * 480)), (255,0,0), 5)
                # cv2.line(image,(0 , 0), (int(point["Middle Tip"].x * 640),int(point["Middle Tip"].y * 480)), (150,0,0), 5)
                
                # making the marks on the hands
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
        
                # FUCTIONS
                # move_mouse(point)
                
                # print(DistanceBetweenTwoPoints(point["Index Tip"],point["Thumb Tip"]))
                # print("ind ",DistanceBetweenTwoPoints(point["Index Tip"],point["Index MCP"]),"\tmid ",DistanceBetweenTwoPoints(point["Middle Tip"],point["Middle MCP"]))
                # print(point["Index Tip"].z)
            
            
                # line
                DrawLine(image,point["Wrist"],point["Middle MCP"],length=3)
            
            # Flip the image horizontally for a selfie-view display.
            # cv2.imshow('MediaPipe Hands',image)

            # shoe the image in the center for thje screen
            winname = "Test"
            cv2.namedWindow(winname)        # Create a named window
            cv2.moveWindow(winname,200,200) 

            # resize image
            image = ResizeWithAspectRatio(image, width=int(gui.size()[0]/2), height=int(gui.size()[1]/2))

            cv2.imshow(winname,image)
            if cv2.waitKey(1) & 0xFF == 27 or cv2.waitKey(1) & 0xFF == ord("q"):
                break




    cap.release()


if __name__ == "__main__":
    main()