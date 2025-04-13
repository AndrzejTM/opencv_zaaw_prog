import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("wiewiorka2.jpg")
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")