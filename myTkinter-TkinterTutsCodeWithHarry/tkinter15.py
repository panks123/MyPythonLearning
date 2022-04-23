'''
Event handling
<Key>
The user pressed any key. The key is provided in the char member of the event object passed to the callback
(this is an empty string for special keys).
'''

from tkinter import *


# function to be called when
# keyboard buttons are pressed
def key_press(event):
    key = event.char
    print(key, 'is pressed')


# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

# here we are binding keyboard
# with the main window
root.bind('<Key>', lambda a: key_press(a))

mainloop()