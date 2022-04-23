from tkinter import *
root=Tk()


text=Label(root,text="HELLO WORLD",font="lucida 500 bold")
scrollbar=Scrollbar(text)
scrollbar.pack(side=RIGHT,fill=Y)
text.pack(fill=BOTH)
scrollbar.config()
root.mainloop()