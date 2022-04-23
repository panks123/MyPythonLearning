'''
Canvas widget---The Canvas widget lets us display various graphics on the application.
It can be used to draw simple shapes to complicated graphs.
We can also display various kinds of custom widgets according to our needs

attributes of Canvas

root = root window.
height = height of the canvas widget.
width = width of the canvas widget.
bg = background colour for canvas.
bd = border of the canvas window.
scrollregion =(w, n, e, s)tuple defined as a region for scrolling left, top, bottom and right
highlightcolor =colour shown in the focus highlight.
cursor =It can defined as a cursor for the canvas which can be a circle, a do, an arrow etc.
confine =decides if canvas can be accessed outside the scroll region.
relief =type of the border which can be SUNKEN, RAISED, GROOVE and RIDGE.

Some common drawing methods

Creating an Oval
 oval = C.create_oval(x0, y0, x1, y1, options)

Creating an arc
 arc = C.create_arc(20, 50, 190, 240, start=0, extent=110, fill="red")

Creating a Line
 line = C.create_line(x0, y0, x1, y1, ..., xn, yn, options)

Creating a polygon
 oval = C.create_polygon(x0, y0, x1, y1, ...xn, yn, options)
'''

from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
canvas_widget=Canvas(root,height=canvas_height,width=canvas_width)
canvas_widget.pack()
# creating a line --here coordinates are:starting point(x1,y1)and end point(x2,y2)
canvas_widget.create_line(0,0,800,400,fill="red")
canvas_widget.create_line(800,0,0,400,fill="red")


# creating a rectangle--- here coordinates of top left(x1,y1) and bottom right(x2,y2)
canvas_widget.create_rectangle(200,100,600,300,fill="blue")
canvas_widget.create_rectangle(300,150,500,250,fill="green")
# creating an oval---here coordinates are of a rectangle's top-left and bottom right in which the oval sits inside
# the rectangle touching the rectangle
canvas_widget.create_oval(300,150,500,250,fill="red")
canvas_widget.create_oval(350,150,450,250,fill="cyan")

# create-text--- here we specify the coordinates of the center
canvas_widget.create_text(400,200,text="Canvas Widget")



root.mainloop()