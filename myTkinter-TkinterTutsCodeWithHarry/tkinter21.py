'''
tkinter21---Scrollbar
for connecting scroll bar to a widget
1. widget( yscrollcommand = scrollbar.set ) ----yscrollcommand for vertical scroll bar
2. scrollbar.config( command = widget.yview )
'''
from tkinter import *


root=Tk()
root.geometry("600x500")
root.title("Scroll bar")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
list_box=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(1,200):
    list_box.insert(END,f"Item {i}")
list_box.pack(pady=17,fill="both")

scrollbar.config(command=list_box.yview)


root.mainloop()