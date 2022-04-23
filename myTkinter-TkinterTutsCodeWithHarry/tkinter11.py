# Event handling---Binding function is used to deal with the events.
# syntax---widget.bind(event, handler)
'''
If an event matching the event description occurs in the widget, the given handler
is called with an object describing the event.

<Button-1>
A mouse button is pressed over the widget. Button 1 is the leftmost button, button 2 is the middle button
(where available), and button 3 the rightmost button. When you press down a mouse button over a widget,
Tkinter will automatically “grab” the mouse pointer, and subsequent mouse events (e.g. Motion and Release events) will
then be sent to the current widget as long as the mouse button is held down, even if the mouse is moved outside the
current widget.The current position of the mouse pointer (relative to the widget) is provided in the x and y
members of the event object passed to the callback.
Note:
    You can use ButtonPress instead of Button, or even leave it out completely: <Button-1>,
    <ButtonPress-1>, and <1> are all synonyms.
'''

from tkinter import *

root = Tk()


def callback(event): # note that the event function will always take a mandatory argument as event
    print(f"Mouse clicked at {event.x, event.y}")

root.geometry("300x400")
btn = Button(root,text="Click here",bg="green",height=3,width=20)
btn.bind("<Button-1>", callback)
btn.pack()

root.mainloop()
