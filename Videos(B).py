import cv2
import numpy as np
img = cv2.imread('image.jpg')
red_channel = img[:, :, 2]
red_img = np.zeros(img.shape)


red_img[:, :, 2] = red_channel
cv2.imshow('hello', red_img)

cv2.imwrite('C:/Users/Darshil Patel/PycharmProjects/ll/frame_at_6_red.jpg', red_img)
cv2.waitKey()