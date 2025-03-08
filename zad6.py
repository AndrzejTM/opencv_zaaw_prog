import cv2

# Wczytaj obraz
image1 = cv2.imread('wiewiorka2.jpg')

# Sprawdzenie, czy obrazy zostały poprawnie wczytane
if image1 is None:
    print("Błąd: Nie udało się wczytać obrazu 1")

# Jeśli oba obrazy są załadowane, wyświetl je w oknach z możliwością zmiany rozmiaru
if image1 is not None:
    # Utwórz okna, które można zmieniać
    cv2.namedWindow('Obraz 1', cv2.WINDOW_NORMAL)

    # Możesz ustawić rozmiar okna ręcznie
    cv2.resizeWindow('Obraz 1', 800, 600)  # Zmieniamy rozmiar okna na 800x600

    # Wyświetl obrazy w oknach
    cv2.imshow('Obraz 1', image1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()