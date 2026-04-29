import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Step 1: Read the image
img = cv2.imread('/content/wallhaven-xl7evz.jpg')

# Check if image loaded properly
if img is None:
    print("Error: Image not found")
else:
    # Step 2: Create a kernel (matrix)
    kernel = np.ones((5,5), np.uint8)

    # Step 3: Apply erosion
    eroded_image = cv2.erode(img, kernel, iterations=1)

    # Step 4: Display original and eroded images
    cv2_imshow(img)
    cv2_imshow(eroded_image)

    # Wait until a key is pressed (not necessary for cv2_imshow, but harmless)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Optional: Save output image
    cv2.imwrite('eroded_output.jpg', eroded_image)
