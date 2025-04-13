import cv2

image = cv2.imread("wiewiorka2.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    print("Podaj wartości startX, endX, startY, endY")

    startX = int(input("Podaj startX (współrzędna początkowa X): "))
    endX = int(input("Podaj endX (współrzędna końcowa X): "))
    startY = int(input("Podaj startY (współrzędna początkowa Y): "))
    endY = int(input("Podaj endY (współrzędna końcowa Y): "))

    roi = image[startY:endY, startX:endX]

    cv2.imshow("Obraz", image)
    cv2.imshow("ROI", roi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
