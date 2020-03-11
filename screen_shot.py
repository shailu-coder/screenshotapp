


import PIL.ImageGrab
#import datetime
from tkinter import *
import time



root = Tk()
root.geometry('440x300')
root.title("Screen_Shot")
############################################# main code

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
