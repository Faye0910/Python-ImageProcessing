import cv2
import tkinter as tk
from PIL import ImageTk,Image

class pic():
    def __init__(self):
        self.img=cv2.imread("picture/123.png") #先讀取檔案
        #cv2.imshow("show",img)  #名字跟要顯示的圖
        cv2.waitKey(0)          #等於0就是不會關掉,1000是停一秒
        GARYIMG=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)  #顯示灰階跟cv2.IMREAD_GRAYSCALE記憶體儲存不同  在二值化要先灰階
        _, aa = cv2.threshold(GARYIMG,225,255,cv2.THRESH_BINARY)    #(輸入的圖片,門檻值,新值,二值化)    "底線,a"是防呆機制  高於門檻變新值  比門檻低變黑
        #cv2.imshow("show2", (aa) )  #名字跟要顯示的圖
        cv2.waitKey(0)          #等於0就是不會關掉,1000是停一秒
        #cv2.imwrite('aaa.jpg',img)  額外存入一張
        #print('ok')
#=====================tkinter================================
        self.window = tk.Tk()
        self.window.title("二值化")
        self.window.geometry('600x480')
        self.label1=tk.Label(self.window,text='123')
        self.label1.pack()
        self.button=tk.Button(self.window,text='確定',command=self.qqq)
        self.button.pack()
        self.window.mainloop()
    def qqq(self):
        try:
            oimg=cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)  #讓圖片從BGR變RGB
            self.eimg=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
            im=Image.fromarray(oimg)                        #放在圖片陣列
            img2=ImageTk.PhotoImage(image=im)               #傳到img2

            if self.label1 is None:
                self.label1=tk.Label(image=img2)
                self.label1.image=img2
                self.label1.pack()
            else:
                self.label1.configure(image=img2)
                self.label1.image = img2
        except:
            print("error 1")

cv2.destroyWindow('show')   #關掉'show'這個視窗

main = pic()