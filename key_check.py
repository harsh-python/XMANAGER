import time
from tkinter import *
import json
from tkinter import messagebox




# reading file
set_file = open('./settings.json','r')
data = set_file.read()
set_file.close()
#setting color
setcolor = json.loads(data)   # loading color
accent_color = setcolor["accent_color"] # font color

# reading file for key
key_file = open('./X_SERVER/pass.json','r')
data = key_file.read()
key_file.close()
#setting key
setkey = json.loads(data)   # loading key
keyname = setkey["key"] # key

#exitnum data
v = {"key":keyname,"exitnum":1}
exit_data = json.dumps(v)
v2 = {"key":keyname,"exitnum":0}
exit_data2 = json.dumps(v2)

# check function for checking the entered key
def check():
    keyc = passbox.get()
    if keyname == keyc:
        messagebox.showinfo("PASSWORD","ENTERED PASSWORD IS CORRECT!!!")
        key_file = open('./X_SERVER/pass.json','w')
        data = key_file.write(exit_data2)
        key_file.close()
        root.destroy()
        exit()
    else:
        messagebox.showerror("PASSWORD","ENTERED PASSWORD IS INCORRECT")
        key_file = open('./X_SERVER/pass.json','w')
        data = key_file.write(exit_data)
        key_file.close()
        root.destroy()
        exit()

def exit1():
    key_file = open('./X_SERVER/pass.json','w')
    data = key_file.write(exit_data)
    key_file.close()
    root.destroy()
    exit()


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

root = Tk()
root.title('LOGIN')
root.iconbitmap(r"./icon.ico")
root.resizable(0,0)
root.geometry("350x350")
root.config(bg="black")
root.overrideredirect(True)


title_lb = Label(root,text='XMANAGER', font=('Modern',56,'bold'))
title_lb.config(bg='black',fg=accent_color)
title_lb.pack()

lb1 = Label(root,text="ENTER PASSWORD")
lb1.config(font=('Modern',15,'bold'),bg='black',fg=accent_color)
lb1.pack(pady=5,padx=5)

# entry for password
passbox = Entry(root,width=40,show="●",justify='center',bg=accent_color,border=0)
passbox.pack(pady=5,padx=5)

#enter button to check the password
bttn(root,"ENTER",20,1,"black",accent_color,check)
bttn(root,"EXIT",15,1,"black",accent_color,exit1)
root.mainloop()