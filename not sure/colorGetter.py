# import cv2
# from time import sleep
# import os
# # Start the webcam
# cap = cv2.VideoCapture(0)


# def SaveColorList(colorlist):
#     filename = 'colorlist.txt'

#     # add Numbmer to filename if it already exists
#     if os.path.isfile(filename):
#         while os.path.isfile(filename):
#             filename = 'colorlist' + str(i) + '.txt'
#             i += 1
#     else:
#         filename = 'colorlist.txt'
    
#     print(filename)

#     with open(filename, 'w') as f:
#         for item in colorlist:
#             f.write("%s," % item)

# color = []
# while True:
#     sleep(0.5)
#     # Read a frame from the webcam
#     ret, frame = cap.read()

#     # Get the size of the frame
#     height, width, _ = frame.shape

#     # Define the size of the square
#     square_size = 25
#     center_x, center_y = width // 2, height // 2

#     # Get the average RGB values of the pixels in the square
#     square = frame[center_y - square_size:center_y + square_size, center_x - square_size:center_x + square_size]
#     avg_rgb = cv2.mean(square)

#     # Print the average RGB values
#     print("R:", avg_rgb[2], "G:", avg_rgb[1], "B:", avg_rgb[0])

#     # store these in a list
#     color.append(avg_rgb)

#     # Draw a rectangle around the square
#     cv2.rectangle(frame, (center_x - square_size, center_y - square_size), (center_x + square_size, center_y + square_size), (255, 0, 0), 2)

#     # Show the frame
#     cv2.imshow('Webcam', frame)

#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         # print(color)
#         break

# # Release the webcam and close the windo


# print("--------------->",avg_color)
# SaveColorList(color)

# cap.release()
# cv2.destroyAllWindows()


import cv2
from time import sleep
import os
import pandas

# Start the webcam
cap = cv2.VideoCapture(0)
df = pandas.DataFrame(columns=["R", "G", "B"])
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Get the size of the frame
    height, width, _ = frame.shape

    # Define the size of the square
    square_size = 25
    center_x, center_y = width // 2, height // 2

    # Get the average RGB values of the pixels in the square
    square = frame[center_y - square_size:center_y + square_size, center_x - square_size:center_x + square_size]
    avg_rgb = cv2.mean(square)

    # Print the average RGB values
    print("R:", avg_rgb[2], "G:", avg_rgb[1], "B:", avg_rgb[0])
    # store in df using concat
    df = pandas.concat([df, pandas.DataFrame({"R": avg_rgb[2], "G": avg_rgb[1], "B": avg_rgb[0]}, index=[0])], ignore_index=True)
    # df = df.concat({"R": avg_rgb[2], "G": avg_rgb[1], "B": avg_rgb[0]}, ignore_index=True)

    # Draw a rectangle around the square
    cv2.rectangle(frame, (center_x - square_size, center_y - square_size), (center_x + square_size, center_y + square_size), (255, 0, 0), 2)

    # Show the frame
    cv2.imshow('Webcam', cv2.flip(frame, 1))


    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(df)

# save this as a csv
# df.to_csv("colorlist.csv")

# df.to_csv("colornlknew.csv", index=False)



# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
