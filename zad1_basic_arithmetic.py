import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread("wiewiorka2.jpg")

# Jasność +50: NumPy
brighter_numpy = image + 50

# Jasność +50: OpenCV
brighter_cv2 = cv2.add(image, np.ones(image.shape, dtype="uint8") * 50)

# Wyświetlenie wyników
cv2.imshow("Oryginalny", image)
cv2.imshow("Jasniejszy - NumPy", brighter_numpy)
cv2.imshow("Jasniejszy - OpenCV", brighter_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
