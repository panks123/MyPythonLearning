'''
More on tkinter
- adding custom icon to the GUI
-adding background to the window
-getting width and height of the screen
'''
from tkinter import *
root=Tk()
root.geometry("467x367")
root.title("More on tkinter")

root.wm_iconbitmap("favicon.ico")

root.configure(background="black")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")

Button(text="Close",command=root.destroy).pack()  # root.destroy() function destroys the window mainloop
root.mainloop()