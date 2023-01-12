import cv2
img=cv2.imread("640x480/1-1.jpg") #先讀取檔案
cv2.imshow("show",img)  #名字跟要顯示的圖
cv2.waitKey(0)          #等於0就是不會關掉,1000是停一秒

GARYIMG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #顯示灰階跟cv2.IMREAD_GRAYSCALE記憶體儲存不同
cv2.imshow("show2",GARYIMG)  #名字跟要顯示的圖
cv2.waitKey(0)          #等於0就是不會關掉,1000是停一秒

#cv2.imwrite('aaa.jpg',img)  額外存入一張
#print('ok')
cv2.destroyWindow('show')   #關掉'show'這個視窗