import cv2
import numpy as np

image = cv2.imread("wiewiorka2.jpg")

image_float = image.astype(np.int16)

image_filtered = image_float.copy()
image_filtered[:, :, 0] += 10   # Blue
image_filtered[:, :, 1] -= 20   # Green
image_filtered[:, :, 2] += 30   # Red

image_filtered = np.clip(image_filtered, 0, 255).astype(np.uint8)

cv2.imshow("Oryginalny", image)
cv2.imshow("Instagram Filter", image_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
