'''
Author: Wei-Ju-Chen(Idonotwant)
ProjectName: Hello_World
Description: A simple Hello_World example for tkinter
Brief_Log:
2022/04/13 Start
Note: 
'''

import sys
import tkinter as tk

#global constants
windowWidth = 600
windowHeight = 400

#tk environment setting
root = tk.Tk()
root.title('Hello World')

root.geometry(f'{windowWidth}x{windowHeight}+0+0')
#root.attributes('-alpha',0.8) #transparency

#tk modules
message1 = tk.Label(root,text="Hello World")
message1.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

#keep the window displaying
root.mainloop()