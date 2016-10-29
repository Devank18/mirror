#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont
from datetime import *

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")
        self.parent = parent
        self.initUI()
            
    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        self.splash()
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=1850, y=1150)
        self.customFont = tkFont.Font(family="Helvetica", size=36)
        label = Label(self, text = datetime.now().strftime('%H:%M:%S'), font = self.customFont)
        label.configure(background='black')
        label.configure(foreground='white')
        label.pack(side='top')
       
    
    def splash(self):
        ws = self.parent.winfo_screenwidth() # width of the screen
        hs = self.parent.winfo_screenheight()
        x = 0
        y = 0
        self.parent.geometry('%dx%d+%d+%d' % (ws, hs, x, y))
 

def main():
  
    root = Tk()
    
    root.wm_attributes('-type', 'splash')
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()

