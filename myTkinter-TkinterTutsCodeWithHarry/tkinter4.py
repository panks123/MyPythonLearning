'''
tkinter4--- Frame widgets (Frames)---A frame is a rectangular region on the screen.
            A frame can also be used as a foundation class to implement complex widgets.
            It is used to organize a group of widgets.

Frames are like <div> in html

Attributes of frame
bg: (background)
height: The vertical dimension of the new frame.
width:
cursor: By using this option, the mouse cursor will change to that pattern when it is over the checkbutton.
'''

from tkinter import *
root=Tk()
root.title("MyTkinter4")
root.geometry("540x380")
frame_f1=Frame(root,bg="blue",borderwidth=3,relief=SUNKEN)#Place the frame  inside root
frame_f1.pack(side=LEFT,fill=Y,padx=12)
frame_f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
frame_f2.pack(side=TOP,fill="x",pady=10)
l1=Label(frame_f1,text="Tkinter4",fg="red",bg="cyan")
l1.pack(pady=50)
l2=Label(frame_f2,text="Welocome To Tkinter4",fg="red",bg="cyan",font="helvetica 16 bold")#Place the label inside frame_f1
l2.pack()
root.mainloop()