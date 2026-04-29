import cv2
from google.colab.patches import cv2_imshow

# Read the image
img = cv2.imread("/content/IMG_20251025_101107_775.jpg")

# Check if image loaded properly
if img is None:
    print("Error: Image not found")

else:
    # Rotate image 90 degrees clockwise
    rotated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display original image
    cv2_imshow(img)

    # Display rotated image
    cv2_imshow(rotated_image)

    # Wait for key press
    # cv2.waitKey(0)

    # Close all windows
    # cv2.destroyAllWindows()

    # Optional: Save rotated output
    cv2.imwrite("rotated_output.jpg", rotated_image)
