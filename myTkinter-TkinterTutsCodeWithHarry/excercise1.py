#excercise1--creating a status bar strip
from tkinter import *
root =Tk()
root.geometry("500x400")
status_bar_label=Label(text="ready...",anchor="w",borderwidth=2,relief=SUNKEN)
status_bar_label.pack(side=BOTTOM,fill=X)
root.mainloop()