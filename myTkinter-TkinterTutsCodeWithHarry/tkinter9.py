from tkinter import *
root=Tk()
root.geometry(f"{310}x{350}")
for i in range(10):
   Label(text=f"{i} ",anchor='nw').pack(side='bottom')
root.mainloop()