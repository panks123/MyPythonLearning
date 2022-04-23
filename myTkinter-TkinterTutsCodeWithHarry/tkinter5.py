'''
tkinter5-- Buttons widget

'''
from tkinter import *
def task():
    print("Hello world")


root=Tk()
root.geometry("634x580")
root.title("MyTkinterButtons")
f1=Frame(root,borderwidth=6,relief=SUNKEN,bg="grey")
f1.pack(side="left",anchor=NW)
b1=Button(f1,fg="blue",text="Click",bg="cyan",command=task) #command attribute will execute the function in its value
b1.pack(side=LEFT,padx=6)
b2=Button(f1,fg="blue",text="Click",bg="red")
b2.pack(side=LEFT,padx=6)
b3=Button(f1,fg="blue",text="Click",bg="cyan")
b3.pack(side=LEFT,padx=6)
b4=Button(f1,fg="blue",text="Click",bg="red")
b4.pack(side=LEFT,padx=6)
b5=Button(f1,fg="blue",text="Click",bg="cyan")
b5.pack(side=LEFT,padx=6)
root.mainloop()