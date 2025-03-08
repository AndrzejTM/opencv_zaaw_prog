import cv2

# Wczytaj obraz
image = cv2.imread('pies.jpg')

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    # Uzyskaj wymiary obrazu (wysokość, szerokość, liczba kanałów)
    height, width, _ = image.shape

    # Oblicz wymiary dla 9 równych części
    part_width = width // 3
    part_height = height // 3

    # Współrzędne środkowej części (fragmentu obejmującego środek obrazu)
    center_x = part_width
    center_y = part_height

    # Wycinamy fragment obrazu obejmujący środek
    cropped_image = image[part_height:2*part_height, part_width:2*part_width]

    # Wyświetl wycięty fragment
    cv2.imshow('Wycięty fragment', cropped_image)

    # Czekaj na naciśnięcie dowolnego klawisza
    cv2.waitKey(0)
    cv2.destroyAllWindows()
