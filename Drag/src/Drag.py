'''
Author: Wei-Ju-Chen(Idonotwant)
ProjectName: Drag
Description: Drag
Brief_Log:
2022/04/23 Start
Note: 
'''
import sys
from tkinter import *
from TkinterDnD2 import DND_FILES,TkinterDnD


class Dragger(TkinterDnD.Tk):
    def __init__(self,*args,**argvs):
        super().__init__()
        self.wm_title('Drag')
        self.configure(background='white')
        self.wm_minsize(800,600)
        self.wm_maxsize(1440,2800)
        self.counter = 1
        self.div_size = 200
        self.div1 = Frame(self)
        self.labelCounter = Label(self.div1,text="0",fg="black")
        self.labelCounter.grid(column=0,row=0)
        self.fileList = Listbox(self.div1,selectmode=SINGLE,background="#ffe0d6")
        self.fileList.grid(column=0,row=1)
        self.fileList.drop_target_register(DND_FILES)
        self.fileList.dnd_bind("<<Drop>>",self.dropIn)

        self.div1.rowconfigure(0,weight=1)
        self.div1.rowconfigure(1,weight=5)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=6)
        self.div1.grid(row=0,column=0)

        print(self.size())

        self.run()
        self.refresh_data()
        self.mainloop()
    def refresh_data(self):
        self.labelCounter.config(text=str(self.counter))
        
        self.counter +=1
        if(len(sys.argv)-1):
            data = sys.argv[1]
            self.labelDragger.config(self,text=data,fg='black')
        self.after(1000,self.refresh_data)
    
    def run(self):
        pass
    
    def dropIn(self,event):
        self.fileList.insert("end",event.data)


if __name__ == '__main__':
    dragger = Dragger()