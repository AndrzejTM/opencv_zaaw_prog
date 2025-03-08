import cv2
import numpy as np

image = cv2.imread('pies.jpg')

# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray_image)

    print(f'Najjaśniejszy piksel ma współrzędne: {max_loc}')
    print(f'Jego wartość jasności: {max_val}')
