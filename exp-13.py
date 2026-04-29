import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('/wallhaven-5gkpe3.jpg')

# Affine matrix for shifting image
M = np.float32([[1,0,50],
                [0,1,50]])

# Apply affine transformation
result = cv2.warpAffine(img, M, (500,500))

cv2_imshow(img)
cv2_imshow(result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
