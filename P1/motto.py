'''
author: Idonotwant
Brief log:
[2022/04/06] Completed
NOTE: LOL Vel'Koz voise(maybe that is not a motto)
    Beginning of Tkinter
'''

import sys
import tkinter as tk

#global constants(handling ctrl+i,Fonts)
ctrlClicked = False
iClicked = False

FONT_REMINDER = ('times',12,'bold')
FONT_MOTTO = ('FreeSerif',20,'bold italic')
FONT_TEXT = ('microsoft yahei',15)

#tk environment setting
root = tk.Tk()
root.title('B09901102_Motto')

windowWidth = 600
windowHeight = 400

root.geometry(f'{windowWidth}x{windowHeight}+{0}+{0}')#upper-left
root.attributes('-alpha',0.8) #transparency

#functions
def keyHandler(event):#handling keyboard 
    global ctrlClicked
    global iClicked
    key = event.keysym
    #print(key)
    if key=='Escape':
        leave()
    elif key=='i':
        if(ctrlClicked):
            enableInputBox()
            iClicked = False
            ctrlClicked = False
        else:
            iClicked = True
    elif key=='Control_L' or key=='Control_R':
        if(iClicked):
            enableInputBox()
            iClicked = False
            ctrlClicked = False
        else:
            ctrlClicked = True
    else:
        if key=='Return':
            getInput()
        iClicked = False
        ctrlClicked = False

def enableInputBox():#enable input box
    print('inputBox abled...')
    inputBox1.config(state='normal')
    inputBox1.focus()

def leave(*args):#click Escape to terminate the program
    print('Leaved...')
    sys.exit()
def getInput(*args):#handling(modify motto) input after clicking 'Return' 
    print("getInput")
    inMotto = inputBox1.get('1.0','end')
    if len(inMotto)-1:
        print(inMotto[:-1])
        messageMotto.configure(text=inMotto[:-1])
    inputBox1.delete('1.0','end')
    inputBox1.config(state=tk.DISABLED)

#tk modules
messageMotto = tk.Label(root,text='Humans:simple, messy, yet exceptional.',font=FONT_MOTTO)
messageMotto.place(relx=0.5,rely=0.5, anchor='center')
message1 = tk.Label(root,text="Click Ctrl+i to Input and Enter to change your motto!",font=FONT_REMINDER,fg='red')
message2 = tk.Label(root,text="Click ESC to leave",font=FONT_REMINDER,fg='red')
message1.pack()
message2.place(relx= 0.0,rely = 1.0,anchor='sw')

inputBox1 = tk.Text(root,height=1,font=FONT_TEXT)
inputBox1.config(state=tk.DISABLED)
inputBox1.pack()

#messageMotto.pack()

root.bind('<KeyRelease>',keyHandler)

#keep the window displaying
root.mainloop()
