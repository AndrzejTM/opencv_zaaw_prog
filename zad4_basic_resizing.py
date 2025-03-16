import cv2
# load the original input image and display it on our screen
image = cv2.imread("wiewiorka2.jpg")
cv2.imshow("Original", image)
# perform the resizing

(h, w) = image.shape[:2]
(cX, cY) = (w * 3, h * 3)
resized = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_AREA)
cv2.imshow("INTER_NEAREST", resized)
resized2 = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_LINEAR)
cv2.imshow("INTER_LINEAR", resized2)
resized3 = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_CUBIC)
cv2.imshow("INTER_CUBIC", resized3)
resized4 = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("INTER_LANCZOS4", resized4)


# Powiększanie obrazu z użyciem metody INTER_LINEAR
# resized_image = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_LINEAR)

# Zapisz lub wyświetl powiększony obraz
# cv2.imshow("200 x 300", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()