import cv2
import numpy as np

image1 = cv2.imread("scena1.jpg")
image2 = cv2.imread("scena2.jpg")

difference = cv2.absdiff(image1, image2)

cv2.imshow("Obraz 1", image1)
cv2.imshow("Obraz 2", image2)
cv2.imshow("Różnica", difference)
cv2.waitKey(0)
cv2.destroyAllWindows()
