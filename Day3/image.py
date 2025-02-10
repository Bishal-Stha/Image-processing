import cv2

image = cv2.imread("./images/ORL(new)/s1/1.pgm")
image = cv2.resize(image,(500,500))

image_blur = cv2.GaussianBlur(image,(25,25),0)

cv2.imshow("Original",image)
cv2.imshow("Output",image_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
