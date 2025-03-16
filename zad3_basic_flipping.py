# import the necessary packages
import cv2
# load the original input image and display it to our screen
image = cv2.imread("wiewiorka2.jpg")
cv2.imshow("Original", image)
# flip the image horizontally
print("[INFO] flipping image vertically and horizontally...")
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Vertically and Horizontally", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()