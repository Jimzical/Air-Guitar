import cv2
import pandas

# Define the range of yellow color in HSV
# lower_yellow = (120, 112, 4)
# upper_yellow = (180, 132, 55)

# df=pandas.read_csv("colorlist.csv")
# lower_yellow = (df["B"].min(), df["G"].min(), df["R"].min())
# upper_yellow = (df["B"].max(), df["G"].max(), df["R"].max())
# lower_yellow = (df["R"].min(), df["G"].min(), df["B"].min())
# upper_yellow = (df["R"].max(), df["G"].max(), df["B"].max())


df = pandas.read_csv("colornew.csv")

# lower_yelow  = (df["B"].min(), df["G"].min(), df["R"].min())
# upper_yelow  = (df["B"].max(), df["G"].max(), df["R"].max())

df = df.describe()
x =-20
y = 80
# lower_yellow = (df["B"]["mean"]+x, df["G"]["mean"]+x, df["R"]["mean"]+x)
# upper_yellow = (df["B"]["mean"]+y, df["G"]["mean"]+y,df["R"]["mean"]+y)
# print(lower_yellow,upper_yellow)
# 
# lower_yellow = (4, 80, 100)
# upper_yellow = q(55, 250, 180)
# Start the webcam


lower_yellow = (20, 40, 4)
upper_yellow = (80, 182, 185)
cap = cv2.VideoCapture(0)

# take a picture using the webcam
ret, framezzz = cap.read()
# show the picture
# cv2.imshow('Webcam', cv2.flip(framezzz, 1))
# cv2.waitKey(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the frame to only select yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # finmask = cv2.inRange(hsv, lower_finger, upper_finger)

    # combined_mask = cv2.bitwise_or(mask, finmask)
    # res = combined_mask

    # Bitwise-AND the mask and the original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # make it so all the pixels that are not yellow are replaced with pixels from the original framezzz
    # res = cv2.bitwise_or(framezzz, res)

    # Show the frame left right inverted
    cv2.imshow('Webcam', cv2.flip(res, 1))
    # cv2.imshow('Webcam', res)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()   
cv2.destroyAllWindows()
