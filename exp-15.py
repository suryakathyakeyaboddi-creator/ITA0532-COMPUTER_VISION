import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Read image
img = cv2.imread('/captain.jpg')

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark corners in red
img[corners > 0.01 * corners.max()] = [0,0,255]

# Display output
cv2_imshow(img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
