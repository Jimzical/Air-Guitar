# This Module is for the Air Guitar Project
# Current Working Version: 2.0
# Features:
# - Detects Thumb and Line Contact
# - Dyanmic Rainbow Gradient list gerneator for lines
# - Proper offset Calculation Done 
# - More Dynamic Points using image shape
# - Proper Fucntions for All the Code
# - Cleaned up the code

# TODO:
# select hands
# Setup music generation
# 


import cv2
import mediapipe as mp
from pyautogui import size
from math import sin, cos, radians, degrees, atan2, sqrt, pi

def rainbow_gradient(num_colors):
    """Returns a list of RGB colors that make a rainbow gradient"""
    colors = []
    for i in range(num_colors):
        r, g, b = 0, 0, 0
        if 0 <= i < num_colors/6:
            r = 255
            g = int(255*i/(num_colors/6))
        elif num_colors/6 <= i < num_colors/3:
            r = 255 - int(255*(i-num_colors/6)/(num_colors/6))
            g = 255
        elif num_colors/3 <= i < num_colors/2:
            g = 255
            b = int(255*(i-num_colors/3)/(num_colors/6))
        elif num_colors/2 <= i < 2*num_colors/3:
            g = 255 - int(255*(i-num_colors/2)/(num_colors/6))
            b = 255
        elif 2*num_colors/3 <= i < 5*num_colors/6:
            r = int(255*(i-2*num_colors/3)/(num_colors/6))
            b = 255
        elif 5*num_colors/6 <= i < num_colors:
            r = 255
            b = 255 - int(255*(i-5*num_colors/6)/(num_colors/6))
        colors.append((r, g, b))
    return colors

def DistanceBetweenTwoPoints(point1, point2):
    dist = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5
    return dist

def ResizeWithAspectRatio(image, width = 1920, height= 1080, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    r = width / float(w)
    dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def initializeCode(hands,cap):
    success, image = cap.read()
    image =  cv2.flip(image, 1)
    if not success:
        print("Ignoring empty camera frame.")
        # TODO: Make it Raise an error Later
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    results = hands.process(image)
    return image, results

def endCode(cap):
    if cv2.waitKey(1) & 0xFF == 27 or cv2.waitKey(1) & 0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        return True
    else:
        return False

def markHands(image, results, point, mp_drawing, mp_drawing_styles, mp_hands):
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

def showImage(image):
    image = ResizeWithAspectRatio(image, width=int(size()[0]/2), height=int(size()[1]/2))
    cv2.imshow('MediaPipe Hands', image)
    return

def DrawLine(image,point1,point2,length = 3 ,xoffset = 0, yoffset = 0 ,Lncolor = (255,0,0) , Hand = True , OneHand = False, log = False,thick=5):
    # TODO: remove the redundant offset code
    if OneHand:
        startpoint = (int(point1.x * image.shape[1]) + xoffset ,int(point1.y * image.shape[0]) + yoffset)
        endpoint = point2
    elif Hand:
        startpoint = (int(point1.x * image.shape[1]) + xoffset ,int(point1.y * image.shape[0]) + yoffset )
        endpoint = (int(point2.x * image.shape[1]) + xoffset ,int(point2.y * image.shape[0]) + yoffset )
        endpoint = (int(endpoint[0] + (endpoint[0] - startpoint[0]) * length),int(endpoint[1] + (endpoint[1] - startpoint[1]) * length))
    else:
        startpoint = point1
        endpoint = point2

    if log:
        print("startpoint: {}, endpoint: {}".format(startpoint,endpoint))
    cv2.line(image, startpoint, endpoint, Lncolor, thickness=thick)
    return startpoint, endpoint

def newPos(image,AnchorStartPoint,AnchorEndPoint,offset = 20,length = 4):
    x1,y1 = int(AnchorStartPoint.x * image.shape[1]), int(AnchorStartPoint.y * image.shape[0])
    x2,y2 = int(AnchorEndPoint.x * image.shape[1]), int(AnchorEndPoint.y * image.shape[0])


    Angle = atan2(y2 - y1, x2 - x1)

    x3 = x1 - offset * cos(pi/2 - Angle)
    y3 = y1 + offset * sin(pi/2 - Angle)

    x3 = int(x3)
    y3 = int(y3)
    
    startpoint = (x3,y3)
    
    x4 = x2 - offset * cos(pi/2 - Angle)
    y4 = y2 + offset * sin(pi/2 - Angle)
    
    x4 = int(x4)
    y4 = int(y4)
    
    endpoint = (x4,y4)

    endpoint = (int(endpoint[0] + (endpoint[0] - startpoint[0]) * length),int(endpoint[1] + (endpoint[1] - startpoint[1]) * length))
    return startpoint, endpoint


def DrawBoard(image, AnchorStartPoint,AnchorEndPoint , lines = 4,xoffset = 20,yoffset =20, offset = 0,dynamic = False,log = False , length = 2, thickness = 4):
    # Draw the board
    col = rainbow_gradient(lines)

    posList = []

    if dynamic:
        offset = (AnchorEndPoint.y - AnchorStartPoint.y) * image.shape[0] / lines

    Stoffset = -(lines//2) * offset

    for stringLine in range(lines):
        start,end = newPos(image,AnchorStartPoint,AnchorEndPoint,offset = Stoffset)
        DrawLine(image, start, end, length=length,Hand=False,log=log,Lncolor=col[stringLine],thick=thickness)
        posList.append((start,end))
        Stoffset += offset

        if log:
            print("String {} => Start {} --> End {}".format(stringLine, start, end))
            # print("PosList: {}",posList)

    return posList

def ContactCheck(image,draw, finger,log = False, accuracy = 10, logSize = 0.75, logColor = (0, 0, 255)):
    thumb_x = int(finger.x * image.shape[1])
    thumb_y = int(finger.y * image.shape[0])
    thumb_z = abs(finger.z) / accuracy
    for GuitarString in range(len(draw)):
        x1 = int(draw[GuitarString][0][0])
        y1 = int(draw[GuitarString][0][1])
        x2 = int(draw[GuitarString][1][0])
        y2 = int(draw[GuitarString][1][1])
        if log:
            print("String {} => Start {} --> End {}".format(GuitarString, (x1, y1), (x2, y2)))
            print("String {} => Start {} --> End {}".format(GuitarString, draw[GuitarString][0], draw[GuitarString][1]))

        if abs((y2 - y1) * thumb_x - (x2 - x1) * thumb_y + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) <= thumb_z:
            # remove any previous text
            cv2.putText(image, " ", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(image, "String {}".format(GuitarString), (100 * (GuitarString), 50), cv2.FONT_HERSHEY_SIMPLEX, logSize, logColor, 1)
        # else:
            # cv2.putText(img, "No Contact", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
# ------------------------------------------------------------------------------------------------
# for debugging
def DrawBoardLog(draw):
    for i in range(len(draw)):
        print("Line {} => Start {} --> End {}".format(i, draw[i][0], draw[i][1]))
def FingerLog(point,finger):
    print("Finger {} => x: {} y: {} z: {}".format(finger,point[finger].x, point[finger].y,point[finger].z))
# ------------------------------------------------------------------------------------------------
def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    # For webcam input:
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
    while cap.isOpened():
        image, results = initializeCode(hands,cap)
        # print(image.shape)
        if results.multi_hand_landmarks:
            point = {"Wrist" : results.multi_hand_landmarks[0].landmark[0] ,"Thumb CMC" : results.multi_hand_landmarks[0].landmark[1], \
                "Thumb MCP" : results.multi_hand_landmarks[0].landmark[2], "Thumb IP" : results.multi_hand_landmarks[0].landmark[3], \
                    "Thumb Tip" : results.multi_hand_landmarks[0].landmark[4], "Index MCP" : results.multi_hand_landmarks[0].landmark[5], \
                        "Index PIP" : results.multi_hand_landmarks[0].landmark[6], "Index DIP" : results.multi_hand_landmarks[0].landmark[7], \
                            "Index Tip" : results.multi_hand_landmarks[0].landmark[8], "Middle MCP" : results.multi_hand_landmarks[0].landmark[9], \
                                "Middle PIP" : results.multi_hand_landmarks[0].landmark[10], "Middle DIP" : results.multi_hand_landmarks[0].landmark[11], \
                                    "Middle Tip" : results.multi_hand_landmarks[0].landmark[12], "Ring MCP" : results.multi_hand_landmarks[0].landmark[13], \
                                        "Ring PIP" : results.multi_hand_landmarks[0].landmark[14], "Ring DIP" : results.multi_hand_landmarks[0].landmark[15], \
                                            "Ring Tip" : results.multi_hand_landmarks[0].landmark[16], "Pinky MCP" : results.multi_hand_landmarks[0].landmark[17], \
                                                "Pinky PIP" : results.multi_hand_landmarks[0].landmark[18], "Pinky DIP" : results.multi_hand_landmarks[0].landmark[19], \
                                                    "Pinky Tip" : results.multi_hand_landmarks[0].landmark[20]}
            
            markHands(image, results, point,mp_drawing,mp_drawing_styles,mp_hands)

            draw = DrawBoard(image, point["Wrist"], point["Middle MCP"], lines=5, offset=20,log=False , dynamic=True)

            ContactCheck(image,draw, point["Thumb Tip"],log = False, accuracy = 5)
        
        showImage(image)
        endCode(cap)
if __name__ == "__main__":
    main()

    