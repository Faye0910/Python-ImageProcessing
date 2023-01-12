import cv2
import numpy as np

cap = cv2.VideoCapture("picture/1.avi")

sum=0
zhen=0
while (1):
    ret, frame = cap.read()
    if not ret:
        break
    frame=frame.astype(np.float32)
    sum+=frame
    zhen=zhen+1
img=sum/zhen
img = img.astype(np.uint8) #轉成整數

cv2.imshow('avg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()