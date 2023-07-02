import cv2
import soundfile as sf
import sounddevice as sd

# create a global variable to store the current sound file data and sample rate
current_data = None
current_samplerate = None

def play_sound(file_path):
    global current_data
    global current_samplerate
    # stop any current sound that is playing
    sd.stop()
    # read the sound file and store the data and sample rate in global variables
    current_data, current_samplerate = sf.read(file_path)
    # play the sound
    sd.play(current_data, current_samplerate)


def PrintEveryNthFrame(n,limit,msg):
    
    if n == limit:
        print(limit," frames have passed--->" + msg)
        n = 0
        return n
    else:
        n += 1
        return n


def SetThreshold(cap):
    # take a picture
    ret, frame = cap.read()
     # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    total_pixels = frame.shape[0] * frame.shape[1]
    # Get the number of yellow pixels
    yellow_pixels = cv2.countNonZero(mask)
    # Calculate the percentage of yellow pixels
    percentage_yellow = (yellow_pixels / total_pixels) * 100
    return percentage_yellow * 0.7 , percentage_yellow * 0.5
# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture(0)

# Set the frame width and height
cap.set(3, 640)
cap.set(4, 480)
# day
# lower_yellow = (4, 80, 100)
# upper_yellow = (55, 250, 180)

# night
lower_yellow = (20, 80, 4)
upper_yellow = (80, 232, 255)

data, samplerate = sf.read("cchord.wav")

n = 0
m = 0
prevPercentage = 0
upper_yellow_threshold,lower_yellow_threshold = SetThreshold(cap)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)


    # Get the total number of pixels in the image
    total_pixels = frame.shape[0] * frame.shape[1]
    # Get the number of yellow pixels
    yellow_pixels = cv2.countNonZero(mask)
    # Calculate the percentage of yellow pixels
    percentage_yellow = (yellow_pixels / total_pixels) * 100

    # Check if the percentage of yellow pixels is greater than or equal to a threshold
    if percentage_yellow >= upper_yellow_threshold:
        cv2.putText(res, "Guitar UNStrummed!", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow("Yellow Color Detection", res)
        
        if prevPercentage < upper_yellow_threshold:
            print("---Guitar UNStrummed")

        prevPercentage = percentage_yellow

    else:
        if percentage_yellow > lower_yellow_threshold:
            play_sound("cchord.wav")

            cv2.putText(frame, "Guitar Strummed!", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

       
        else:
            cv2.putText(frame, "No Guitar Detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("Yellow Color Detection", frame)
        if prevPercentage >= upper_yellow_threshold:
            print("Guitar Strummed" + str(percentage_yellow))

        prevPercentage = percentage_yellow




    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
