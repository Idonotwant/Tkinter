'''
Author: Wei-Ju-Chen(Idonotwant)
ProjectName: Drag
Description: Drag
Brief_Log:
2022/04/23 Start
Note: A great(?) GUI for user to Drop in files and record its paths(abs) in self.filePaths
'''
import sys
from tkinter import *
import tkinter.messagebox as mesbox #show message in different window
from TkinterDnD2 import DND_FILES,TkinterDnD
alignmode = "nswe"
REFRESHRATE = 1000


class Dragger(TkinterDnD.Tk):
    def __init__(self,*args,**argvs):
        super().__init__()
        #basic setting
        self.wm_title('Drop')
        self.configure(background='white')
        self.wm_minsize(800,600)
        self.wm_maxsize(self.winfo_screenwidth(),self.winfo_screenheight())
        #top level grid
        self.div1 = Frame(self,bg='green')
        self.div1.grid(row=0,column=0,sticky=alignmode)
        #clock
        self.counter = 1
        self.labelCounter = Label(self.div1,text="0",fg="black")
        self.labelCounter.grid(column=0,row=0,sticky=alignmode)
        #fileList : a listBox to see files selected
        self.fileList = Listbox(self.div1,selectmode=SINGLE,background="#ffe0d6")
        self.fileList.grid(column=0,row=1,sticky=alignmode)
        self.fileList.drop_target_register(DND_FILES)
        self.fileList.dnd_bind("<<Drop>>",self.dropIn)
        self.filePaths = []
        #div1 childs
        self.div1.rowconfigure(0,weight=1)
        self.div1.rowconfigure(1,weight=5)
        self.div1.columnconfigure(0,weight=1)
        #root childs
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        #event listener
        ##leaving
        self.bind('<Escape>',self.leave)
        self.protocol("WM_DELETE_WINDOW", self.leave)
    #automatically refresh window per refreshrate(ms)
    def refresh_data(self):
        self.labelCounter.config(text=str(self.counter))
        self.counter +=1
        self.after(REFRESHRATE,self.refresh_data)
    #instead of running immediately agter creating OBJ,I use this function
    def run(self,*args):
        self.refresh_data()
        #refresh window per action!!
        self.mainloop()
    #you can do things before leaving
    def leave(self,*args):
        print("exc")
        #mesbox.showwarning(title='警告', message='点击了关闭按钮')
        self.destroy()
        
    #If a file is dropped in
    def dropIn(self,event):
        self.fileList.insert("end",event.data)
        self.filePaths.append(event.data)


if __name__ == '__main__':
    a = Dragger()
    a.run()
    