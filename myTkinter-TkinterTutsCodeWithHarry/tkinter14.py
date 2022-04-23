'''
Event Handling
<Enter>
The mouse pointer entered the widget
'''

from tkinter import *

root = Tk()


def mouse_enter(event):
    print('Mouse entered at x = % d, y = % d'%(event.x, event.y))


root.geometry("300x400")
frame1 = Frame(root, height = 100, width = 200,borderwidth=4,relief=SUNKEN)
frame1.bind("<Enter>", mouse_enter)
frame1.pack()

root.mainloop()
'''
<Leave>
The mouse pointer left the widget.

<Return>
The user pressed the Enter key. You can bind to virtually all keys on the keyboard. 
For an ordinary 102-key PC-style keyboard, the special keys are Cancel (the Break key), BackSpace, Tab, 
Return(the Enter key), Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, 
Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, 
F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.


'''