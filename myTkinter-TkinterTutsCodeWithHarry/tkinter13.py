'''
Event Handling
<Double-Button-1>
Button 1 was double clicked.
You can use Double or Triple as prefixes. Note that if you bind to both a single click (<Button-1>) and a double click,
both bindings will be called.
'''

from tkinter import *

root = Tk()


def double_click(event):
    print('Double clicked at x = % d, y = % d'%(event.x, event.y))


root.geometry("300x400")
btn = Button(root,text="Click here",bg="green")
btn.bind("<Double-Button-1>", double_click)
btn.pack()

root.mainloop()
