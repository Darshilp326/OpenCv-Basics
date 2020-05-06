import cv2
img = cv2.imread('flowers.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
image[:, :, 3] = 0.5
cv2.imwrite('C:/Users/Darshil Patel/PycharmProjects/ll/alpha-channel.png', image)
cv2.imshow('image', image)
x = cv2.imread('alpha-channel.png')

cv2.imshow('original',x)
cv2.waitKey(0)
