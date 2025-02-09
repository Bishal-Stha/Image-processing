import cv2

image = cv2.imread('./batman.png')
image = cv2.resize(image,(600,600))

blur_image = cv2.GaussianBlur(image,(25,25),0)

cv2.imshow("Blur Batman Logo",blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
