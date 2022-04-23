#practing for grid

import sys
from tkinter import *


startwidth = 600
startheight = 600
pad = 2
alignmode = 'nswe'


class tester(Tk):
    def __init__(self,*args,**argvs):
        super().__init__()
        self.wm_title("Grid Practice")
        self.config(background='white')
        self.wm_maxsize(self.winfo_screenwidth(),self.winfo_screenheight())
        self.wm_minsize(startwidth,startheight)

        self.f1 = Frame(self,width=startwidth,height=startheight/2,bg='green')
        self.f1.grid(column=0,row=0,sticky=alignmode)


        self.f2 = Frame(self,width=startwidth,height=startheight/2,bg="blue")
        self.f2.grid(column=0,row=1,sticky=alignmode)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)



if __name__ == "__main__":
    a = tester()
    a.mainloop()