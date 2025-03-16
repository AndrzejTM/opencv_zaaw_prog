import cv2
import numpy as np

height, width = 500, 500
image = np.zeros((height, width, 3), dtype=np.uint8)

start_point = (width // 2, height // 2)
end_point = (width - 1, height - 1)

color = (255, 0, 0)
thickness = 2
cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow("Line Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
