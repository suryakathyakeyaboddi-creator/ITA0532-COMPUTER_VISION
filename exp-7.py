import cv2
import time
from google.colab.patches import cv2_imshow

# Read the captured video
video = cv2.VideoCapture('sample_video.mp4')

# Check whether video opened successfully
if not video.isOpened():
    print("Error opening video file")

while video.isOpened():
    ret, frame = video.read()

    if ret == True:

        # Display video
        cv2_imshow(frame)

        # ---- Slow Motion Effect ----
        # Delay increased (0.1 sec)
        time.sleep(0.1)

        # ---- Fast Motion Effect ----
        # Skip frames for fast effect
        video.read()
        video.read()

        # Press q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

# Release video object
video.release()
cv2.destroyAllWindows()
