'''
tkinter19---Radio buttons
'''
from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order recieved",f"We have received your order for {var.get()}\n\nThanks for your order.\n\n "
    f"We will be back to you soon")
root=Tk()
root.geometry("600x500")
root.title("Radio buttons")
# var=IntVar()
var=StringVar()
# var.set("Samosa")
var.set(" ")
Label(root,text="What would you like to have?",font="lucida 15 bold",padx=14,pady=15,justify=LEFT).pack()

radio=Radiobutton(root,text="Dosa",variable=var,value="Dosa",padx=14).pack(anchor="w")
radio=Radiobutton(root,text="Paratha",variable=var,value="Paratha",padx=14).pack(anchor="w")
radio=Radiobutton(root,text="Samosa",variable=var,value="Samosa",padx=14).pack(anchor="w")
radio=Radiobutton(root,text="Kachori",variable=var,value="Kachori",padx=14).pack(anchor="w")

Button(text="Order now",command=order).pack()
root.mainloop()