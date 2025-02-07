import cv2

# Load the image
image = cv2.imread("download.jpg")# Replace with your image file

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

# Show original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Blurred Image", blurred_image)

# Save the grayscale image
cv2.imwrite("grayscale_image.jpg", gray_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
