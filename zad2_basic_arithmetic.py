import cv2
import numpy as np

image = cv2.imread("wiewiorka2.jpg")

burned_numpy = image + 150

burned_cv2 = cv2.add(image, np.ones(image.shape, dtype="uint8") * 150)

cv2.imshow("Oryginalny", image)
cv2.imshow("Przepalenie - NumPy", burned_numpy)
cv2.imshow("Przepalenie - OpenCV", burned_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
