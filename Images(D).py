import cv2

img = cv2.imread('horse.jpg')
I = 0.3 * img[:, :, 2] + 0.59 * img[:, :, 1] + 0.11 * img[:, :, 0]
cv2.imwrite("horse_gray.jpg", I)
