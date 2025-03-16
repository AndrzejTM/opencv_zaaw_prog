import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('wiewiorka2.jpg')

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

# Odbicie poziome (lustrzane w poziomie)
horizontal_flip = cv2.flip(image, 1)

# Odbicie pionowe (lustrzane w pionie)
vertical_flip = cv2.flip(image, 0)

# Odbicie względem obu osi (odwrócenie poziome i pionowe)
both_flip = cv2.flip(image, -1)

# Wyświetlenie czterech wersji obrazu
cv2.imshow("Oryginał", image)
cv2.imshow("Odbicie poziome", horizontal_flip)
cv2.imshow("Odbicie pionowe", vertical_flip)
cv2.imshow("Odbicie względem obu osi", both_flip)

# Czekaj na naciśnięcie klawisza i zamknij okna
cv2.waitKey(0)
cv2.destroyAllWindows()
