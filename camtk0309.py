import cv2
from PIL import ImageTk,Image
import threading
import tkinter as tk

class cam():
    def __init__(self):
        self.frame=[]
        self.abc = True
    def camtest(self):
        # self.cam1=cv2.VideoCapture(0)        #開啟攝影機
        self.cam1 = cv2.VideoCapture("picture/123.mp4")  # 讀影片

        while (True):  # 讀影片都用while處理
            if (self.abc == True):
                self.status, self.frame = self.cam1.read()  # 讀
            if self.status == False:
                break
            # ===============================時間==============================
            time = self.cam1.get(cv2.CAP_PROP_POS_MSEC)
            print(time)

            oimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(oimg)
            img2 = ImageTk.PhotoImage(image=im)
            self.label1.configure(image=img2)
            if self.label1 is None:
                self.label1 = tk.Label(image=img2)
                self.label1.image = self.img2
                self.label1.pack()
            else:
                self.label1.configure(image=img2)
                self.label1.image = img2
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cam1.release()
            cv2.destroyAllWindows()

    def start(self):
        self.cam1 = cv2.VideoCapture(0)
        threading.Thread(target=self.camtest, daemon=True).start()

    def stop(self):
        cv2.waitKey(1)
        self.cam1.release()
        cv2.destroyAllWindows()

    def stoop(self):
        if (self.abc == True):
            self.abc = False
        else:
            self.abc = True


main=cam().camtest()