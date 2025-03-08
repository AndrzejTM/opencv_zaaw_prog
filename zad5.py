import cv2

# Wczytaj dwa obrazy
image1 = cv2.imread('wiewiorka2.jpg')
image2 = cv2.imread('wiewiorka2_gray.jpg')

# Wyświetl obrazy w osobnych oknach
cv2.imshow('Obraz 1', image1)
cv2.imshow('Obraz 2', image2)

# Czekaj na naciśnięcie dowolnego klawisza w obu oknach
cv2.waitKey(0)  # Zatrzymuje działanie programu, czeka na naciśnięcie klawisza

# Zamknij wszystkie okna
cv2.destroyAllWindows()