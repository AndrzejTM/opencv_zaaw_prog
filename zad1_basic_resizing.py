import cv2
# load the original input image and display it on our screen
image = cv2.imread("wiewiorka2.jpg")
cv2.imshow("Original", image)
# perform the resizing

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
resized = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()