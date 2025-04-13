import cv2

image = cv2.imread("wiewiorka2.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    height, width = image.shape[:2]

    half_width = width // 2

    right_half = image[:, half_width:width]

    cv2.imshow("Prawa połowa obrazu", right_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
