import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('/wallhaven-5gkpe3.jpg')

# Flip vertically and horizontally = 180 rotation
rotated = cv2.flip(image, -1)

cv2_imshow(rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
