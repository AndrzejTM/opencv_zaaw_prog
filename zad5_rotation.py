# import the necessary packages
import argparse
import imutils
import cv2
# load the image and show it
image = cv2.imread("wiewiorka2.jpg")
cv2.imshow("Original", image)
# grab the dimensions of the image and calculate the center of the
# image

# kat = int(input("Podaj kąt obrotu"))
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
# cX = 0
# cY = 0
kat = 180
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), kat, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated by 30 Degrees", rotated)
# rotate our image by -90 degrees around the image
# M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by kat Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()