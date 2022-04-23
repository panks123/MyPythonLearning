'''
tkinter23---status bar
Statusbar is not a widget we will create a status bar with the help of Label widget.
'''
from tkinter import *

# function to update the status bar when it performs  function


def upload():
    statusVar.set("Uploading...")
    statusBar.update()  # to update the widget without this statement the above lines will not be executed to optimize
    # the code
    import time
    time.sleep(2)
    statusVar.set("Ready")

root=Tk()
root.geometry("600x500")
root.title("Status bar")

statusVar=StringVar()
statusVar.set("Ready")
statusBar=Label(root,textvariable=statusVar,relief=SUNKEN,anchor=W)
statusBar.pack(side=BOTTOM,fill=X)

Button(root,text="Upload",command=upload).pack(pady=50)
root.mainloop()