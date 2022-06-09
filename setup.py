import time
from tkinter import *
import json
import os
import shutil

# creating folders
os.system("md X_SERVER")
os.system("md J")
os.system("move J .//X_SERVER")
os.system('attrib +h +s +r X_SERVER')
file = open("settings.json","w")
file.close()
file = open("./X_SERVER/pass.json","w")
file.close()
shutil.copyfile("./icon.ico","./X_SERVER/icon.ico")
shutil.move('./key_check.py','./X_SERVER/key_check.py')

class Setup:
    def __init__(self,user,color,key) -> None:
        self.user = user
        self.color = color
        self.key = key

    def set_user(self):
        #reading file
        self.v2 = {
            "accent_color":self.color,
            "username":self.user
        }
        self.name_data = json.dumps(self.v2)
        # print(name_data)
        self.file = open("settings.json",'w')
        self.data = self.file.write(self.name_data)
        self.file.close()
    def set_accent(self):
        # reading file
        self.v = {
            "accent_color":self.color,
            "username":self.user
        }
        self.name_data = json.dumps(self.v)
        # print(name_data)
        self.file = open("settings.json",'w')
        self.data = self.file.write(self.name_data)
        self.file.close()
    def set_key(self):
        # reading file
        self.v = {
            "key":self.key,
            "exitnum":0
        }
        self.name_data = json.dumps(self.v)
        # print(name_data)
        self.file = open("./X_SERVER/pass.json",'w')
        self.data = self.file.write(self.name_data)
        self.file.close()


def bttn(win,text,w,h,bcolor,fcolor,cmd):

        def on_enter(e):
            b1['background'] = bcolor
            b1['foreground'] = fcolor
        def on_leave(e):
            b1['background'] = fcolor
            b1['foreground'] = bcolor


        b1 = Button(win,width=w,height=h,text=text,
                fg=bcolor,
                bg=fcolor,
                border=0,
                relief='groove',
                activeforeground=fcolor,
                activebackground=bcolor,
                font=('Courier New',12,'bold'),
                command=cmd)
        b1.pack(pady=5)
        b1.bind('<Enter>',on_enter)
        b1.bind('<Leave>',on_leave)

def set1():
            name = input2.get()
            num = input3.get()
            set1 = Setup(name,accent_color,num)
            set1.set_user()
            set1.set_accent()
            set1.set_key()
            input2.delete(0,'end')
            time.sleep(1)
            shutil.copyfile("./settings.json","./X_SERVER/settings.json")
            root.destroy()

username = "ADMIN"
accent_color = "white"
key1 = "1234"

def setw():
    global accent_color
    accent_color = "white"
def setg():
    global accent_color
    accent_color = "green"
def setr():
    global accent_color
    accent_color = "red"

# main window
root = Tk()
root.title('XMANAGER SETUP')
root.geometry('950x500')
root.iconbitmap(r".//icon.ico")
# root.resizable(False,False)

# window configure
root.config(bg="black")



# Labels
title_lb = Label(root,text='XMANAGER SETUP', font=('Modern',56,'bold'))
title_lb.config(bg='black',fg='white')
title_lb.pack()

atitle_lb = Label(root,text="Hi!"+" "+"USER", font=('Modern',20,'bold'))
atitle_lb.config(bg='black',fg='white')
atitle_lb.pack()

atitle_lb2 = Label(root,text="ENTER YOUR NAME", font=('Modern',15,'bold'))
atitle_lb2.config(bg='black',fg='white')
atitle_lb2.pack()

input2 = Entry(root,bg="white",width=40,justify='center',border=0)
input2.pack(pady=10,padx=10)

atitle_lb4 = Label(root,text="ENTER YOUR PASSWORD", font=('Modern',15,'bold'))
atitle_lb4.config(bg='black',fg='white')
atitle_lb4.pack()

input3 = Entry(root,bg="white",width=40,show="●",justify='center',border=0)
input3.pack(pady=10,padx=10)

atitle_lb3 = Label(root,text="SELECT YOUR COLOR", font=('Modern',15,'bold'))
atitle_lb3.config(bg='black',fg='white')
atitle_lb3.pack()
bttn(root,"WHITE",29,1,"black","white",setw)
bttn(root,"GREEN",29,1,"black","white",setg)
bttn(root,"RED",29,1,"black","white",setr)
bttn(root,"SET",20,1,"black","white",set1)

root.mainloop()
