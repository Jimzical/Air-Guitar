# professional python tutorial
# for webcam input

import cv2
import mediapipe as mp

# cap = cv2.VideoCapture(0)
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils

class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.FingerDictionary = {"Wrist": 0, "Thumb_MCP": 1, "Thumb_IP": 2, "Thumb_Tip": 3, "Index_MCP": 4, "Index_PIP": 5,"Index_DIP": 6, "Index_Tip": 7, "Middle_MCP": 8, "Middle_PIP": 9, "Middle_DIP": 10, "Middle_Tip": 11, "Ring_MCP": 12, "Ring_PIP": 13, "Ring_DIP": 14, "Ring_Tip": 15, "Pinky_MCP": 16, "Pinky_PIP": 17, "Pinky_DIP": 18, "Pinky_Tip": 19,"Thumb_TMC": 20}
        self.AxisDictionary = {"X": 0, "Y": 1, "Z": 2}
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image

    def positionFinder(self,image, handNo=0, draw=True, pointSize=4):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])

                cv2.putText(image, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, lm.z * -25, (0, 0, 0), 1)

            # if draw:
                # cv2.circle(image,(cx,cy), pointSize , (0,255,0), cv2.FILLED)

        return lmlist

    def Gestures(self, image, lmList, draw=True):
        if len(lmList) != 0:
            # Thumb
            if lmList[self.FingerDictionary["Thumb_Tip"]][self.AxisDictionary["Y"]] > lmList[self.FingerDictionary["Thumb_MCP"]][self.AxisDictionary["Y"]]:
                cv2.putText(image, "Thumb Up", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # # Index
            # elif lmList[self.FingerDictionary["Index_Tip"]][self.AxisDictionary["Y"]] < lmList[self.FingerDictionary["Index_MCP"]][self.AxisDictionary["Y"]]:
            #     cv2.putText(image, "Index Up", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # # Middle
            # elif lmList[self.FingerDictionary["Middle_Tip"]][self.AxisDictionary["Y"]] < lmList[self.FingerDictionary["Middle_MCP"]][self.AxisDictionary["Y"]]:
            #     cv2.putText(image, "Middle Up", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # # Ring
            # elif lmList[self.FingerDictionary["Ring_Tip"]][self.AxisDictionary["Y"]] < lmList[self.FingerDictionary["Ring_MCP"]][self.AxisDictionary["Y"]]:
            #     cv2.putText(image, "Ring Up", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # # Pinky
            # elif lmList[self.FingerDictionary["Pinky_Tip"]][self.AxisDictionary["Y"]] < lmList[self.FingerDictionary["Pinky_MCP"]][self.AxisDictionary["Y"]]:
            #     cv2.putText(image, "Pinky Up", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

def main():
    cap = cv2.VideoCapture(0)
    tracker = handTracker()

    while True:
        success,image = cap.read()
        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        
        # check gesture
        tracker.Gestures(image, lmList)




        cv2.imshow("Video",image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

if __name__ == "__main__":
    main()