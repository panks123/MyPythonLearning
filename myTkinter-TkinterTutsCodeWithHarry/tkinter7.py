'''
Grid layout in Tkinter

Tkinter possess three layout managers:
1.pack--places the widgets in relative position from the master window
2.grid
3.place
The three layout managers pack, grid, and place should never be mixed in the same master window!

The Grid geometry manager puts the widgets in a 2-dimensional table.
The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget.

'''
from tkinter import *

def takeValues():
    print(userVal.get())
    print(passVal.get())

root=Tk()
root.geometry("456x567")
root.title("MyTkinter7")
user=Label(root,text="Username: ")
password=Label(root,text="Password: ")
user.grid(row=0,padx=10) #row=0 and col=0 is the default value
password.grid(row=1,padx=10)
'''
The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
Variables can be used with most entry widgets to track changes to the entered value.
The Checkbutton and Radiobutton widgets require variables to work properly.

'''
userVal=StringVar()
passVal=StringVar()
userEntry=Entry(root,textvariable=userVal)
passEntry=Entry(root,textvariable=passVal,show='*')
userEntry.grid(row=0,column=1,padx=10,pady=10)
passEntry.grid(row=1,column=1)
Button(text="Submit",command=takeValues).grid(padx=10,pady=10) # note:root is the default master window

root.mainloop()