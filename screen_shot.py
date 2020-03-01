# # import numpy as np
# # import cv2
# # from PIL import ImageGrab
# # img = ImageGrab.grab(bbox=(10, 10, 1350, 700)) #x, y, w, h
# # img_np = np.array(img)
# # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
# # cv2.imshow("frame", frame)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# ######################## normal code

# # pip install pyautogui

# import pyautogui
# import time

# ################ modulenotFoundError: no module named 'pyautogui'
# # for linux or ubuntu type following command:

# # pip3 install python3-xlib
# # sudo apt-get install scrot
# # sudo apt-get install python3-tk
# # sudo apt-get install python3-dev
# # pip3 install pyautogui

# # for windows user follow these steps:

# # pip install --upgrade pip
# # pip install xlib
# # pip install easytkinter
# # pip install aiotkinter
# # pip install mttkinter
# # pip install tkinter.help
# # pip install tkinterhtml


# # pip install autopy



# pyautogui.screenshot('hello.png')



###################################################


import PIL.ImageGrab
#import datetime
from tkinter import *
import time



root = Tk()
root.geometry('440x300')
root.title("Screen_Shot")
############################################# main code

########################################## trying block

# baby = datetime.datetime.now().strftime("%H:%M:%S")
# print(type(baby))
# self.hide = 10 #minutes
# self.show = 10 #seconds
# root.destroy()
############################################
def take_ss():
    root.withdraw()########## it will hide the window we can use there destroy but this will destroy the application and come out from the execution of a program
############################################
    time.sleep(1)
    img=PIL.ImageGrab.grab()
    img.save("hello.png")
    # root.withdraw()
############################################to back the window
    root.update()
    root.deiconify()

    
#############################################

Button(root, text='Take Shot',width=25,height=4,bg='brown',fg='white', command=take_ss).place(x=130,y=120)
Label_1=Label(root, text="</Developed By:-Shailendra kumar/> \n DM me for further querry:www.facebook/shailendrakr007   ", width=80, font=("bold",9))
Label_1.place(x=-8,y=260)



root.mainloop()