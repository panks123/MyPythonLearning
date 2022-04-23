# excercise 2---Window resizer

from tkinter import *


def apply_resize():
    root.geometry(f"{width_val.get()}x{height_val.get()}")


root=Tk()
root.title("Excercise 2 - Window Resizer")
Label(root,text="Enter width of window:",padx=5,pady=5).grid(row=1,column=1)
width_val=IntVar()
height_val=IntVar()
width=Entry(root,textvariable=width_val)
width.grid(row=1,column=2)
Label(root,text="Enter height of window:",padx=5,pady=5).grid(row=2,column=1)
height=Entry(root,textvariable=height_val)
height.grid(row=2,column=2)
Button(text="Click to Apply",bg="cyan",fg="blue",command=apply_resize,pady=5).grid(row=3,column=2,pady=5)
root.mainloop()