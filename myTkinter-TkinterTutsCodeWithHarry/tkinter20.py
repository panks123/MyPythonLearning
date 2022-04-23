'''
tkinter20--List box widget

Attrributes:

root – root window.
bg – background colour
fg – foreground colour
bd – border
height – height of the widget.
width – width of the widget.

Common methods:

yview – allows the widget to be vertically scrollable.
xview – allows the widget to be horizontally scrollable.
get() – to get the list items in a given range.
delete(start, last) – delete lines in the specified range.
insert() -
'''

from tkinter import *

i=0
def add():
    global i
    list_box.insert(ACTIVE,f"{i+1}")  # ACTIVE means the item is placed before the item we select in the listbox
    i+=1


root=Tk()
root.geometry("600x500")
root.title("List box")

list_box=Listbox(root,bg="cyan",fg="blue")
list_box.pack()
list_box.insert(END,"first item of the list box")  # END means adds at the end of the list box

Button(root,text="Add,item",command=add).pack()
root.mainloop()
