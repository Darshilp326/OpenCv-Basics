import cv2

cap = cv2.VideoCapture('RoseBloom.mp4')
cap.set(cv2.CAP_PROP_POS_MSEC, 6000)      # Go to the 1 sec. position
ret,frame = cap.read()                   # Retrieves the frame at the specified second
cv2.imwrite("image.jpg", frame)          # Saves the frame as an image
cv2.imshow("Frame Name",frame)           # Displays the frame on screen
cv2.waitKey()