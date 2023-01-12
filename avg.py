'''import numpy as np
import cv2
image = cv2.imread("lena.bmp")
cv2.imshow("Original",image)
cv2.waitKey(0)

#R、G、B分量的提取
(B,G,R) = cv2.split(image)#提取R、G、B分量
#R、G、B的合并
print((B,G,R))
cv2.waitKey(0)'''
'''import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取圖檔
img = cv2.imread('lena.bmp')

# 轉為灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 計算直方圖每個 bin 的數值
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.bar(0,255,int(hist))
plt.show()'''
'''
import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.bmp', 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread('lena.bmp')
HSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
def getpos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(HSV[y,x])
#th2=cv2.adaptiveThreshold(imagegray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("imageHSV",HSV)
cv2.imshow('image',image)
cv2.setMouseCallback("imageHSV",getpos)
cv2.waitKey(0)
#print (image(10,10,10))'''
import cv2
import numpy as np


img=cv2.imread('640x480/1-3.jpg',cv2.IMREAD_COLOR)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower=np.array([0,43,46])
upper=np.array([255,255,255])
mask=cv2.inRange(hsv,lower,upper)
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("hsv",mask)
cv2.waitKey(0)