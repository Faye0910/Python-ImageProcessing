import numpy as np
import cv2

image = cv2.imread('640x480/1-2.jpg')        #原圖

blured=cv2.medianBlur(image, 5)

mean=cv2.blur(image, (5, 5))         #全部平均 5*5個模糊

blurred = np.hstack([ image,blured,mean])

#cv2.imshow('Original', image)
#cv2.imshow('Median', blured)
cv2.imshow('Original+Median+Mean',blurred)

cv2.waitKey(0)


