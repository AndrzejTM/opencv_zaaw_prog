import cv2
import numpy as np

image = cv2.imread("wiewiorka2.jpg")

darker_numpy = image - 80

darker_cv2 = cv2.subtract(image, np.ones(image.shape, dtype="uint8") * 80)

cv2.imshow("Oryginalny", image)
cv2.imshow("Przyciemniony - NumPy", darker_numpy)
cv2.imshow("Przyciemniony - OpenCV", darker_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
