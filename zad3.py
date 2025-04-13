import cv2
image_gray = cv2.imread("wiewiorka2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
(h, w, c) = image_gray.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')