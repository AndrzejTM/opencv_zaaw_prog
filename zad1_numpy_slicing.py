import cv2

# Wczytanie obrazu z pliku
image = cv2.imread("wiewiorka2.jpg")

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    roi = image[0:100, 0:100]

    cv2.imshow("ROI - 100x100 z lewego górnego rogu", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

