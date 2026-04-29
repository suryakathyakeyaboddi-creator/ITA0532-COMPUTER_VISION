import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('/wallhaven-5gkpe3.jpg')

# 270° clockwise rotation (90° counterclockwise)
rotated = cv2.transpose(img)
rotated = cv2.flip(rotated, 0)

cv2_imshow(rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
