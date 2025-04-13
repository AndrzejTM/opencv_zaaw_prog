import cv2

image = cv2.imread("wiewiorka2.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    height, width = image.shape[:2]

    height_div = height // 3
    width_div = width // 3

    parts = []
    for i in range(3):
        for j in range(3):
            part = image[i * height_div:(i + 1) * height_div, j * width_div:(j + 1) * width_div]
            parts.append(part)

            cv2.imshow(f"Część {i*3 + j + 1}", part)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
