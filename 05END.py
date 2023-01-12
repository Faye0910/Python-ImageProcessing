import tkinter as tk
import tkinter.ttk as ttk
import cv2
from PIL import ImageTk,Image
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np

class aa():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("05end")
        self.window.geometry('800x700')

        self.window.bind("<Motion>", self.printcoords)

        self.v = tk.IntVar()
        self.v.set(2)
        self.H11=0
        self.H22=360
        self.H33=0
        self.H44=255
        self.H55=0
        self.H66=255
        self.pic=False
#======================================================================================
        self.tabControl = ttk.Notebook(self.window)
        self.tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab, text='讀檔')
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='二值化')
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='灰階')
        self.tab3=ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='HSV')
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab4, text='直方圖')
#====================================主頁===============================================
        self.label = tk.Label(self.tab, text='請選擇檔案')
        self.label.pack()

        self.button = tk.Button(self.tab, text="匯入檔案", command=self.open_file).pack()
        self.button11 = tk.Button(self.tab, text="停止", command=self.cccc).pack()
        self.textbox1 = tk.Entry(self.tab, width=30)
        self.textbox1.pack()

        tk.Button(self.tab, text="輸出", command=self.print).pack()
        self.label4 = tk.Label(self.tab, text='').pack()
#====================================第一頁================================================
        self.label1 = tk.Label(self.tab1, text='')
        self.label1.pack()
        self.label3 = tk.Label(self.tab1, text='')
        self.label3.pack()

        self.r1 = tk.Radiobutton(self.tab1, text='取最大值', variable=self.v,value=1).pack(anchor='w')
        self.r2 = tk.Radiobutton(self.tab1, text='取最小值', variable=self.v,value =2).pack(anchor='w')
        s = tk.Scale(self.tab1, label='門檻', from_=0, to=255, orient=tk.HORIZONTAL,
                     length=400, tickinterval=255, resolution=1, command=self.per1)
        s.pack()
        self.tabControl.pack(expand=1, fill="both")

#====================================第2頁=================================================
        self.tabControl.pack(expand=1, fill="both")
#===================================第3頁====================================================
        H1 = tk.Scale(self.tab3, from_=0, to=180, orient=tk.HORIZONTAL,
                     length=200, tickinterval=180, resolution=1, command=self.H1).grid(column=0,row=0)

        H2 = tk.Scale(self.tab3, from_=0, to=180, orient=tk.HORIZONTAL,
                      length=200, tickinterval=180, resolution=1, command=self.H2)
        H2.set(180)
        H2.grid(column=0, row=1)
        self.label10 = tk.Label(self.tab3, text='------------------------------------------')
        self.label10.grid(column=0,row=2)

        H3 = tk.Scale(self.tab3, from_=0, to=255, orient=tk.HORIZONTAL,
                      length=200, tickinterval=255, resolution=1, command=self.H3).grid(column=1, row=0)

        H4 = tk.Scale(self.tab3, from_=0, to=255, orient=tk.HORIZONTAL,
                      length=200, tickinterval=255, resolution=1, command=self.H4)
        H4.set(255)
        H4.grid(column=1, row=1)

        self.label11 = tk.Label(self.tab3, text='-------------------------------------------')
        self.label11.grid(column=1, row=2)

        H5 = tk.Scale(self.tab3, from_=0, to=255, orient=tk.HORIZONTAL,
                      length=200, tickinterval=255, resolution=1, command=self.H5).grid(column=2, row=0)

        H6 = tk.Scale(self.tab3, from_=0, to=255, orient=tk.HORIZONTAL,
                      length=200, tickinterval=255, resolution=1, command=self.H6)
        H6.set(255)
        H6.grid(column=2, row=1)

        self.label12 = tk.Label(self.tab3, text='')
        self.label12.grid(column=0, row=5)

        #=========================================================================================
        tk.Button(self.tab4, text="直方", command=self.printfun).pack()
        self.label5 = tk.Label(self.tab4, text='').pack()


        self.window.mainloop()
    def per1(self,a):

        self.aaa=a
        self.label1.config(text='目前門檻值 ' + a)

        try:
            if(self.v.get()==1):
                _, aa = cv2.threshold(self.GARYIMG, int(a), 255, cv2.THRESH_BINARY_INV)
            if (self.v.get()==2):
                _, aa = cv2.threshold(self.GARYIMG, int(a), 255, cv2.THRESH_BINARY)
            im = Image.fromarray(aa)
            img2 = ImageTk.PhotoImage(image=im)
            self.label3.configure(image=img2)
            self.label3.image = img2
        except ValueError:
            tk.messagebox.showinfo(message="是否已載入檔案")

    def print(self):
        a = self.textbox1.get()
        self.img1 = cv2.imread(a)
        self.img = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(self.img)  # 放在圖片陣列
        img22 = ImageTk.PhotoImage(image=im)
        self.label4 = tk.Label(self.tab, image=img22)
        self.label4.image = img22
        self.label4.pack()

        self.hsv = cv2.cvtColor(self.img1, cv2.COLOR_BGR2HSV)
        self.GARYIMG = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        im = Image.fromarray(self.GARYIMG)
        img2 = ImageTk.PhotoImage(image=im)
        self.label2 = tk.Label(self.tab2, image=img2)
        self.label2.image = img2
        self.label2.pack()
        self.pic = True

    def open_file(self):
        filename = filedialog.askopenfilename(title='開啟檔案')
        self.textbox1.insert('insert', filename)

    def printfun(self):
        plt.hist(self.GARYIMG.ravel(), 256,[0,256])
        plt.show()

    def H1(self,a):
        self.H11=a
        if (self.H11 == 360 and self.H22 == 0):
            self.H11 = 0
            self.H22 = 360
        lower = np.array([int(a), int(self.H33), int(self.H55)])
        upper = np.array([int(self.H22), int(self.H44), int(self.H66)])
        print(lower)
        print(upper)
        print('===================')
        mask = cv2.inRange(self.hsv, lower, upper)
        res = cv2.bitwise_and(self.img1, self.img1, mask=mask)
        floatimg=res.astype(np.uint8)
        floatimg = cv2.cvtColor(floatimg, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(floatimg)
        img2 = ImageTk.PhotoImage(image=im)
        self.label12.configure(image=img2)
        self.label12.image = img2

    def H2(self,a):
        self.H22=a
        if (self.H11 == 360 and self.H22 == 0):
            self.H11 = 0
            self.H22 = 360
        lower = np.array([int(self.H11), int(self.H33), int(self.H55)])
        upper = np.array([int(a), int(self.H44), int(self.H66)])
        mask = cv2.inRange(self.hsv, lower, upper)
        res = cv2.bitwise_and(self.img1, self.img1, mask=mask)

        floatimg = res.astype(np.uint8)
        floatimg = cv2.cvtColor(floatimg, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(floatimg)
        img2 = ImageTk.PhotoImage(image=im)
        self.label12.configure(image=img2)
        self.label12.image = img2
    def H3(self,a):
        self.H33 = a
        if (self.H33 == 255 and self.H44 == 0):
            self.H33 = 0
            self.H44 = 255
        lower = np.array([int(self.H11), int(a), int(self.H55)])
        upper = np.array([int(self.H22), int(self.H44), int(self.H66)])
        mask = cv2.inRange(self.hsv, lower, upper)
        res = cv2.bitwise_and(self.img1, self.img1, mask=mask)

        floatimg = res.astype(np.uint8)
        floatimg = cv2.cvtColor(floatimg, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(floatimg)
        img2 = ImageTk.PhotoImage(image=im)
        self.label12.configure(image=img2)
        self.label12.image = img2
    def H4(self,a):
        self.H44 = a
        if (self.H33 == 255 and self.H44 == 0):
            self.H33 = 0
            self.H44 = 255
        lower = np.array([int(self.H11), int(self.H33), int(self.H55)])
        upper = np.array([int(self.H22), int(a), int(self.H66)])
        mask = cv2.inRange(self.hsv, lower, upper)
        res = cv2.bitwise_and(self.img1, self.img1, mask=mask)
        floatimg = res.astype(np.uint8)
        im = Image.fromarray(floatimg)
        img2 = ImageTk.PhotoImage(image=im)
        self.label12.configure(image=img2)
        self.label12.image = img2
    def H5(self,a):
        self.H55 = a
        if (self.H55 == 255 and self.H66 == 0):
            self.H55 = 0
            self.H66 = 255
        lower = np.array([int(self.H11), int(self.H33), int(a)])
        upper = np.array([int(self.H22), int(self.H44), int(self.H66)])
        mask = cv2.inRange(self.hsv, lower, upper)
        res = cv2.bitwise_and(self.img1, self.img1, mask=mask)
        floatimg = res.astype(np.uint8)
        floatimg = cv2.cvtColor(floatimg, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(floatimg)
        img2 = ImageTk.PhotoImage(image=im)
        self.label12.configure(image=img2)
        self.label12.image = img2
    def H6(self,a):
        self.H66 = a
        if (self.H55 == 255 and self.H66 == 0):
            self.H55 = 0
            self.H66 = 255

        lower = np.array([int(self.H11), int(self.H33), int(self.H55)])
        upper = np.array([int(self.H22), int(self.H44), int(a)])

        mask = cv2.inRange(self.hsv, lower, upper)
        res = cv2.bitwise_and(self.img1, self.img1, mask=mask)
        floatimg = res.astype(np.uint8)
        floatimg = cv2.cvtColor(floatimg, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(floatimg)
        img2 = ImageTk.PhotoImage(image=im)
        self.label12.configure(image=img2)
        self.label12.image = img2

    def printcoords(self,event):
        try:
            if (self.pic):
                R = self.img[event.y][event.x][0]
                g = self.img[event.y][event.x][1]
                b = self.img[event.y][event.x][2]
                print(R, g, b)
        except ValueError:
            print('no')

    def cccc(self):
        self.pic=False


main=aa()