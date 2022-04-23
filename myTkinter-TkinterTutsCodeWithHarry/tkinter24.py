'''
Using objects and classes to create GUIs
'''
from tkinter import *

# class that inherits the Tk class


class GUI(Tk):
    def __init__(self):  # here root=Tk() is replaced by self
        super().__init__()  # make sure that constructor of super class is called
        self.geometry("570x359")

    def status(self):
        self.statusVar = StringVar()
        self.statusVar.set("Ready")
        self.statusBar=Label(self,textvariable=self.statusVar,relief=SUNKEN,anchor=W,padx=10)
        self.statusBar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Button clicked")

    def createButton(self,inptext):
        Button(text=inptext,command=self.click).pack()


if __name__ == '__main__':
    window=GUI()   # here root=Tk() is replaced by window
    window.status()
    window.createButton("Click here")
    window.mainloop()

