import cv2

image = cv2.imread("wiewiorka2.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    przyciety_obraz = image[0:300, 0:300]

    cv2.imwrite("przyciety_obraz.jpg", przyciety_obraz)

    print("Przycięty obraz zapisano jako 'przyciety_obraz.jpg'.")

    cv2.imshow("Przycięty obraz", przyciety_obraz)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
