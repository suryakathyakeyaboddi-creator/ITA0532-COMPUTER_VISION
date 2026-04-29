import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Read the image
img = cv2.imread("/content/wallhaven-xl7evz.jpg")

# Check whether image loaded properly
if img is None:
    print("Error: Image not found")
else:

    # Create kernel (structuring element)
    kernel = np.ones((5,5), np.uint8)

    # Apply dilation
    dilated_image = cv2.dilate(img, kernel, iterations=1)

    # Display original image
    cv2_imshow(img)

    # Display dilated image
    cv2_imshow(dilated_image)

    # Wait until key press (not necessary for cv2_imshow, but harmless)
    # cv2.waitKey(0)

    # Close all windows (not necessary for cv2_imshow, but harmless)
    # cv2.destroyAllWindows()

    # Optional: Save output image
    cv2.imwrite("dilated_output.jpg", dilated_image)
