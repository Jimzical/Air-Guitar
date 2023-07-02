import cv2
# from mediapipe.framework import calc_sess
from mediapipe.framework import calculator_pb2

# Load the pre-trained hand detection graph.
calculator_graph_config_file = (
    "mediapipe/models/hand_detection.pbtxt")
# sess = calculator_pb2.CalculatorSession(calculator_graph_config_file)
sess = calculator_pb2.CalculatorOptions(calculator_graph_config_file)

# Open the webcam for capturing video.
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    height, width, _ = frame.shape

    # Run the hand detection model.
    hand_landmarks = sess.run_cuda_inference(
        input_data=frame,
        input_tensor_info=["input_image_tensor:0"],
        output_tensors=["output_keypoints:0"])

    # Draw the hand landmarks on the frame.
    for hand_landmark in hand_landmarks:
        for point in hand_landmark.keypoints:
            x, y = int(point.x * width), int(point.y * height)
            cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hand Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
