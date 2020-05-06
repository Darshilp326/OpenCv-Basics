import cv2
import numpy as np
img = cv2.imread('cat.jpg')
r = img.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0


cv2.imshow('hello', r)

cv2.imwrite('C:/Users/Darshil Patel/PycharmProjects/ll/red-channel.jpg', r)

cv2.waitKey()

