import cv2

image = cv2.imread("batman.png")
image = cv2.resize(image,(800,600))
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

photo = cv2.imread("best_performer_02.jpg")
resized_photo = cv2.resize(photo,(800,600))
gray_scale_photo = cv2.cvtColor(resized_photo,cv2.COLOR_BGR2GRAY)
blur_photo = cv2.GaussianBlur(gray_scale_photo,(25,25),0)

cv2.imshow("Real Batman Logo",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Gray-scaled Batman Logo",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Blur Gray-scaled Batman Logo",blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("best_performer_gray_scale.png",gray_scale_photo)
cv2.imwrite("best_performer_blur_image.png",blur_photo)

cv2.imshow("Black and White",gray_scale_photo)
cv2.imshow("Blur",blur_photo)

cv2.waitKey(0)
cv2.destroyAllWindows()