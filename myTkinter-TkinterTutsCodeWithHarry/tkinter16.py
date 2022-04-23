'''
Menus and submenus in tkinter

'''

from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("Menus and submenus")


def file_command():
    print("Options are not available")


def saveCommand():
    print("Save command executed")


def saveAsCommand():
    print("Save As command executed")


def printCommand():
    print("Print command executed")

def refreshCommand():
    print("Refresh command executed")


def openCommand():
    print("Open command executed")



def copyAllCommand():
    print("copy all executed")


def clearAllCommand():
    print("clear all command executed")


def undoCommand():
    print("undo command executed")

def redoCommand():
    print("redo command executed")


def deleteCommand():
    print("Delete command executed")
'''
Creating non-dropdown menu
'''
# my_menu = Menu(root)
# my_menu.add_command(label="File",command=file_command)
# my_menu.add_command(label="Exit",command=quit) # add_command function performs the specified command when we click on the menu


'''
Creting dropdown menu(Menu with sub menu)
'''
my_menu=Menu(root) # for creating the menu bar
m1=Menu(my_menu,tearoff=0)  # tear0ff=0 will remove the tearoff option ,its default value is 1 which a tearoff line
m1.add_command(label="Save",command=saveCommand)
m1.add_command(label="Save As",command=saveAsCommand)
m1.add_command(label="Print",command=printCommand)
m1.add_separator()  # this adds a separator line --this is used  keep similar options together
m1.add_command(label="Refresh",command=refreshCommand)
m1.add_command(label="Open",command=openCommand)

my_menu.add_cascade(label="File",menu=m1)

m2 = Menu(my_menu)
m2.add_command(label="Copy all",command=copyAllCommand)
m2.add_command(label="Clear all",command=clearAllCommand)
m2.add_command(label="Undo",command=undoCommand)
m2.add_command(label="Redo",command=redoCommand)
m2.add_command(label="Delete",command=deleteCommand)

my_menu.add_cascade(label="Edit",menu=m2)


my_menu.add_command(label="Exit", command=quit)

root.config(menu=my_menu)
root.mainloop()
