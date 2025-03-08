import cv2

# Wczytaj obraz w odcieniach szarości
image = cv2.imread('wiewiorka2.jpg', cv2.IMREAD_GRAYSCALE)

# Zapisz obraz w skali szarości jako nowy plik
cv2.imwrite('wiewiorka2_gray.jpg', image)

print("Obraz zapisany jako nowy plik.")