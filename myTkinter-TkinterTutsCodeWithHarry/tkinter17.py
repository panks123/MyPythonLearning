'''
tkinter-17---Message box---dialog box,yes no box etc.
syntax--messagebox.Function_Name(title, message [, options])

Available Function_Name:
There are functions or methods available in the messagebox widget.

showinfo(): Show some relevant information to the user.
showwarning(): Display the warning to the user.
showerror(): Display the error message to the user.
askquestion(): Ask question and user has to answered in yes or no.
askokcancel(): Confirm the user’s action regarding some application activity.
askyesno(): User can answer in yes or no for some action.
askretrycancel(): Ask the user about doing a particular task again or not.

For more press ctrl and  visit: https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
'''
from tkinter import *
import tkinter.messagebox as tmsg

def help():
    tmsg.showinfo(title="help",message="This is a help box")


def rate():
    value=tmsg.askquestion(title="rate us",message="Was your experience good")
    print(value)
    if value=="yes":
        msg="Great. Happy to serve."
    else:
        msg="We are trying to fix all the issues"
    tmsg.showinfo("Experience",msg)


root=Tk()
root.geometry("800x700")
root.title("Message box")
my_menu=Menu(root) # for creating the menu bar

my_menu.add_command(label="Help",command=help)
my_menu.add_command(label="Rate us",command=rate)
my_menu.add_command(label="Exit", command=quit)


root.config(menu=my_menu)
root.mainloop()