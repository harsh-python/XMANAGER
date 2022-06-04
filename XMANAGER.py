"""
XMANAGER
Server Based File Manager
"""
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import shutil
import time



# main dir
CURR_DIR = os.getcwd()
goto_dir = '\X_SERVER\J'
main_dir = CURR_DIR+goto_dir

try:
    # button with style
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



    # json setting file
    import json
    # reading file
    set_file = open('settings.json','r')
    data = set_file.read()
    set_file.close()
    #setting color
    setcolor = json.loads(data)   # loading color
    accent_color = setcolor["accent_color"] # font color
    # print(accent_color)
    #                                  changing color
    #                           changing color setting class
    class Changecolor:
        def __init__(self, a_color): # a_color is accent_color
            self.a_color = a_color

        def change(self):
            # reading file
            self.v = {
                "accent_color":self.a_color,
                "username":username
            }
            self.name_data = json.dumps(self.v)
            # print(name_data)
            self.file = open("settings.json",'w')
            self.data = self.file.write(self.name_data)
            self.file.close()

    class Changeuser:
        def __init__(self, user):
            self.user = user

        def change_user(self):
            #reading file
            self.v2 = {
                "accent_color":accent_color,
                "username":self.user
            }
            self.name_data = json.dumps(self.v2)
            # print(name_data)
            self.file = open("settings.json",'w')
            self.data = self.file.write(self.name_data)
            self.file.close()

    #username
    # reading file
    set_file = open('settings.json','r')
    data = set_file.read()
    set_file.close()
    #setting color
    name = json.loads(data)   # loading name
    username = name["username"]

    # main window functions
    def add_file():
        def add_file1():
            try:
                filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",
                                    filetypes = (("All files","*.*"),("Text files","*.txt*")))
                target = main_dir+'\\'+os.path.basename(filename)
                # print(target)
                shutil.move(filename,target)
                messagebox.showinfo('FILE MOVED!!','YOUR FILE'+" {"+os.path.basename(filename)+"} "+"IS MOVED TO THE SERVER")
            except:
                messagebox.showerror("ERROR!","CAN'T FIND PATH")
            
        def folder():
            try:
                filename = filedialog.askdirectory(initialdir="/",title="SELECT FOLDER")
                target = main_dir+'\\'+os.path.basename(filename)
                # print(target)
                shutil.move(filename,target)
                messagebox.showinfo('FOLDER MOVED!!','YOUR FOLDER'+" {"+os.path.basename(filename)+"} "+"IS MOVED TO THE SERVER")
            except:
                messagebox.showerror("ERROR!","CAN'T FIND PATH")

        def close_add():
            root_file.destroy()

        root_file = Tk()
        root_file.title('ADD +')
        root_file.geometry('250x200')
        root_file.iconbitmap(r".//icon.ico")
        root_file.resizable(0,0)
        root_file.config(bg='black')

        # stay on the top func
        try:
            def stay_on_top():
                root_file.lift()
                root_file.after(2000, stay_on_top)
        except:
            pass

        bttn(root_file,'ADD FILE',20,1,'black',accent_color,add_file1)
        bttn(root_file,'ADD Folder',20,1,'black',accent_color,folder)
        bttn(root_file,'CLOSE',10,1,'black',accent_color,close_add)
        stay_on_top()
        root_file.mainloop()

    def del_file_folder():
        root_file = Tk()
        root_file.title('DELETE x')
        root_file.geometry('250x200')
        root_file.iconbitmap(r".//icon.ico")
        root_file.resizable(0,0)
        root_file.config(bg='black')

        def del_file():
            try:
                filename = filedialog.askopenfilename(initialdir = main_dir,title = "Delete a File",
                                    filetypes = (("All files","*.*"),("Text files","*.txt*")))
                os.remove(filename)
                messagebox.showinfo('FILE DELETED!!','YOUR FILE'+" {"+os.path.basename(filename)+"} "+"IS DELETED FROM THE SYSTEM")
            except:
                messagebox.showerror("ERROR!","CAN'T FIND PATH")

        def del_folder():
            try:
                filename = filedialog.askdirectory(initialdir=main_dir,title="SELECT FOLDER")
                os.rmdir(filename)
                messagebox.showinfo('FOLDER DELETED!!','YOUR FOLDER'+" {"+os.path.basename(filename)+"} "+"IS DELETED FROM THE SYSTEM")
            except:
                messagebox.showerror("ERROR!","CAN'T FIND PATH")

        def close_del():
            root_file.destroy()
        try:
            def stay_on_top():
                root_file.lift()
                root_file.after(2000, stay_on_top)
        except:
            pass

        bttn(root_file,'DEL FILE',20,1,'black',accent_color,del_file)
        bttn(root_file,'DEL Folder',20,1,'black',accent_color,del_folder)
        bttn(root_file,'CLOSE',10,1,'black',accent_color,close_del)
        stay_on_top()
        root_file.mainloop()
        


    def remove_file():
        def rem_file1():
            try:
                filename = filedialog.askopenfilename(initialdir = main_dir,title = "Select a File",
                                    filetypes = (("All files","*.*"),("Text files","*.txt*")))
                print(filename)
                target = 'C:'+'\\'+os.path.basename(filename)
                # print(target)
                shutil.move(filename,target)
                messagebox.showinfo('FILE REMOVED!!','YOUR FILE'+" {"+os.path.basename(filename)+"} "+"IS MOVED OUT OF THE SERVER, IT IS MOVED IN THE C DRIVE")
            except:
                messagebox.showerror("ERROR!","CAN'T FIND PATH")
            
        def rem_folder():
            try:
                filename = filedialog.askdirectory(initialdir=main_dir,title="SELECT FOLDER")
                target = 'C:'+'\\'+os.path.basename(filename)
                # print(target)
                shutil.move(filename,target)
                messagebox.showinfo('FOLDER REMOVED!!','YOUR FOLDER'+" {"+os.path.basename(filename)+"} "+"IS MOVED OUT OF THE SERVER, IT IS MOVED IN THE C DRIVE")
            except:
                messagebox.showerror("ERROR!","CAN'T FIND PATH")
                
        def close_rem():
            root_file.destroy()

        root_file = Tk()
        root_file.title('REMOVE -')
        root_file.geometry('250x200')
        root_file.iconbitmap(r".//icon.ico")
        root_file.resizable(0,0)
        root_file.config(bg='black')
        # stay on the top func
        try:
            def stay_on_top():
                root_file.lift()
                root_file.after(2000, stay_on_top)
        except:
            pass

        bttn(root_file,'REMOVE FILE',20,1,'black',accent_color,rem_file1)
        bttn(root_file,'REMOVE Folder',20,1,'black',accent_color,rem_folder)
        bttn(root_file,'CLOSE',10,1,'black',accent_color,close_rem)
        stay_on_top()
        root_file.mainloop()

    def exit_main():
        root.destroy()

    def set_color_win():
        #for buttons
        # for close_btn:
        def on_enter(e):
                    close_btn['background'] = 'black'
                    close_btn['foreground'] = accent_color
        def on_leave(e):
                    close_btn['background'] = accent_color
                    close_btn['foreground'] = 'black'
        def exit_1():
            root3.destroy()
        def set_accent():
                def white():
                    color1 = 'white'
                    num = Changecolor(color1)
                    num.change()
                    

                def green():
                    color2 = 'green'
                    num2 = Changecolor(color2)
                    num2.change()
                    

                def red():
                    color3 = 'red'
                    num2 = Changecolor(color3)
                    num2.change()
                
                root2 = Tk()
                root2.config(bg='black')
                root2.title('Accent Setting')
                root2.iconbitmap(r".//icon.ico")
                root2.geometry('250x200')
                root2.resizable(False,False)
                
                # # color buttons
                # b1 = Button(root2,text='WHITE', command=white)
                # b1.config(bg='black',fg=accent_color)
                # b1.pack(pady=5)

                # b2 = Button(root2,text='GREEN', command=green)
                # b2.config(bg='black',fg=accent_color)
                # b2.pack(pady=5)

                # b3 = Button(root2,text='RED', command=red)
                # b3.config(bg='black',fg=accent_color)
                # b3.pack(pady=5)
                bttn(root2,"WHITE",20,1,"black",accent_color,white)
                bttn(root2,"GREEN",20,1,"black",accent_color,green)
                bttn(root2,"RED",20,1,"black",accent_color,red)
                
                root2.mainloop()



        root3 = Tk()
        root3.config(bg='black')
        root3.title('Settings')
        root3.geometry('250x200')
        root3.iconbitmap(r".//icon.ico")
        root3.resizable(False,False)

        def username_ch():
            rootu = Tk()
            rootu.config(bg='black')
            rootu.title('Username Setting')
            rootu.iconbitmap(r".//icon.ico")
            rootu.geometry('400x250')
            rootu.resizable(False,False)

            def set2():
                name = input2.get()
                set1 = Changeuser(name)
                set1.change_user()
                input2.delete(0,'end')

            text_lb = Label(rootu,text='ENTER YOUR USERNAME', font=('Modern',24,'bold'))
            text_lb.config(bg='black',fg=accent_color)
            text_lb.pack()
            input2 = Entry(rootu,bg=accent_color,width=40)
            input2.pack(pady=10,padx=10)
            bttn(rootu,"SET",20,1,"black",accent_color,set2)

            rootu.mainloop()
        
        bttn(root3,"SET ACCENT",20,1,"black",accent_color,set_accent)
        bttn(root3,"CHANGE NAME",20,1,"black",accent_color,username_ch)
        close_btn = Button(root3,width=10,height=1,text="CLOSE",
                    fg="black",
                    bg=accent_color,
                    border=0,
                    relief='groove',
                    activeforeground=accent_color,
                    activebackground="black",
                    font=('Courier New',12,'bold'),
                    command=exit_1)
        close_btn.pack(pady=10)
        close_btn.bind('<Enter>',on_enter)
        close_btn.bind('<Leave>',on_leave)
        l1 = Label(root3,text='TO Save Changes REOPEN THE XMANAGER')
        l1.config(bg='black',fg=accent_color)
        l1.pack(pady=10)

        root3.mainloop()



    def show_files_rec():
        root_rec = Tk()
        root_rec.title('File Records')
        # root_rec.iconbitmap(r'python.ico')
        root_rec.geometry("800x600")
        root_rec.iconbitmap(r".//icon.ico")

        # query_label = Label(root_rec, text=pnt_rec)
        # query_label.grid(row=0, column=0, columnspan=2)
        my_frame = Frame(root_rec)
        my_frame.pack(pady=5)

        # create scrollbar for text box
        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        text_scroll2 = Scrollbar(my_frame, orient='horizontal')
        text_scroll2.pack(side=BOTTOM, fill=X)

        # create text box
        my_text = Text(my_frame, width=122, height=45, font=("Courier New", 13,'bold'), foreground="black", selectbackground="gray", selectforeground="blue", undo=True, yscrollcommand=text_scroll.set, xscrollcommand=text_scroll2.set, wrap="none")
        my_text.pack()

        my_text.delete("1.0", END)
        prec = os.listdir(main_dir)
        list1 = [prec]
        my_text.insert(END, list[prec])

        # Configuring scrollbar
        text_scroll.config(command=my_text.yview)

        text_scroll2.config(command=my_text.xview) 

        root_rec.mainloop() 


    # main window
    root = Tk()
    root.title('XMANAGER')
    root.geometry('950x500')
    root.iconbitmap(r".//icon.ico")
    # root.resizable(False,False)

    # window configure
    root.config(bg="black")



    # Labels
    title_lb = Label(root,text='XMANAGER', font=('Modern',56,'bold'))
    title_lb.config(bg='black',fg=accent_color)
    title_lb.pack()

    atitle_lb = Label(root,text="Hi!"+" "+username, font=('Modern',20,'bold'))
    atitle_lb.config(bg='black',fg=accent_color)
    atitle_lb.pack()

    #buttons
    bttn(root,"SETTINGS",35,1,"black",accent_color,set_color_win)
    bttn(root,"ADD +",35,1,"black",accent_color,add_file)
    bttn(root,"REMOVE -",35,1,"black",accent_color,remove_file)
    bttn(root,"DELETE",35,1,"black",accent_color,del_file_folder)
    bttn(root,"LIST",35,1,"black",accent_color,show_files_rec)
    bttn(root,"EXIT",20,1,"black",accent_color,exit_main)

    root.mainloop()
except:
    messagebox.showerror("ERROR","PLEASE SETUP FIRST XMANAGER")