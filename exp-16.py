import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Step 1: Read the image
image = cv2.imread('/content/IMG_20251025_101143_035.jpg')

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Sobel in X direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Step 4: Apply Sobel in Y direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Step 5: Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Step 6: Combine both directions
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Step 7: Display results
cv2_imshow(image)
cv2_imshow(sobel_x)
cv2_imshow(sobel_y)
cv2_imshow(sobel_combined)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
