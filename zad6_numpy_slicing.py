import cv2

image = cv2.imread("wiewiorka2.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")


    fragment = image[0:100, 0:100]


    image[300:400, 300:400] = fragment

    cv2.imshow("Obraz po wklejeniu fragmentu", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
