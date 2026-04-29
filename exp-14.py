import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('/captain.jpg')

rows, cols, ch = img.shape

# Perspective matrix
M = np.float32([[1,0.2,0],
                [0.2,1,0],
                [0.001,0.001,1]])

# Apply perspective transform
result = cv2.warpPerspective(img, M, (cols, rows))

cv2_imshow(img)
cv2_imshow(result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
