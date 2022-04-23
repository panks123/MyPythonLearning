'''
Event Handling
<B1-Motion>
The mouse is moved, with mouse button 1 being held down (use B2 for the middle button,
B3 for the right button). The current position of the mouse pointer is provided in the x and y
members of the event object passed to the callback.

this event is for-- when we click on the widget and move the mouse
'''

from tkinter import *

root = Tk()

def callback(event):
    print(f"Mouse clicked at {event.x, event.y}")


root.geometry("300x400")
btn = Button(root,text="Click here",bg="green")
btn.bind("<B1-Motion>", callback)
btn.pack()

root.mainloop()
