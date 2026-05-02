import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/IMG_20251025_101143_035.jpg')

if img is None:
    print("Error: Image not found.")
else:
    # Create dummy watermark
    wm_size = 150
    watermark = np.full((wm_size, wm_size, 3), 255, dtype=np.uint8) # White background
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "WATERMARK"
    (text_w, text_h), _ = cv2.getTextSize(text, font, 0.5, 1)
    cv2.putText(watermark, text, ((wm_size - text_w) // 2, (wm_size + text_h) // 2), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Get dimensions and position watermark at bottom-right
    h_img, w_img, _ = img.shape
    h_wm, w_wm, _ = watermark.shape
    x, y = w_img - w_wm - 10, h_img - h_wm - 10

    # Apply watermark
    img[y:y+h_wm, x:x+w_wm] = cv2.addWeighted(img[y:y+h_wm, x:x+w_wm], 0.7, watermark, 0.3, 0)

    cv2_imshow(img)
    cv2.imwrite("watermarked_output.jpg", img)
