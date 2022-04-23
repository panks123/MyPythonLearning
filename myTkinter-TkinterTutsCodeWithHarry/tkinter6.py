'''
Button inside Label
'''


from tkinter import *
root=Tk()
root.geometry("544x389")
root.title("MyTkinter6")
label=Label(root,bg="cyan")
label.pack(side=LEFT,anchor=N,padx=10,pady=20,fill=Y)
b=Button(label,text="Click")
b.pack()
root.mainloop()