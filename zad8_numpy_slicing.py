import cv2

image = cv2.imread("wiewiorka2.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    roi_width = 100
    roi_height = 100

    height, width = image.shape[:2]

    startX = 0
    startY = 0

    delay = 100

    while startX + roi_width <= width:

        roi = image[startY:startY + roi_height, startX:startX + roi_width]

        cv2.imshow("ROI - Przesuwanie kamery", roi)

        key = cv2.waitKey(delay)

        if key == 27:
            break

        startX += 10

    cv2.destroyAllWindows()
