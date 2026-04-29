import cv2
from google.colab.patches import cv2_imshow

# Read the image
img = cv2.imread("/content/IMG_20251025_101107_775.jpg")

# Check if image loaded
if img is None:
    print("Error: Image not found")
else:

    # Enlarge image (Scaling Up)
    bigger_image = cv2.resize(img, None, fx=2, fy=2)

    # Reduce image (Scaling Down)
    smaller_image = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Display original image
    cv2_imshow(img)

    # Display scaled up image
    cv2_imshow(bigger_image)

    # Display scaled down image
    cv2_imshow(smaller_image)

    # Wait for key press
    # cv2.waitKey(0)

    # Close all windows
    # cv2.destroyAllWindows()
