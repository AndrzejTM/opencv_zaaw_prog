import cv2
import imutils

# Wczytanie obrazu
image = cv2.imread('wiewiorka2.jpg')

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

# Zmiana szerokości na 500 pikseli, zachowując proporcje
resized_image = imutils.resize(image, width=500)

# Zapisz lub wyświetl powiększony obraz
cv2.imshow("Zmniejszony obraz", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()