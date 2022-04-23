'''
tkinter3----Attributes of  Label and Pack
Label---Tkinter Label is a widget that is used to implement display boxes where you can place text or images.
---Attributes of Label
image: This option is used to display a static image in the label widget.

text: This option is used to display a text in the label widget.

bg:(background) This option is used to set the normal background color displayed behind the label and indicator.

fg:(foreground) The label color, used for text and bitmap labels. The default is system specific. If you are displaying
   a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.

font:If you are displaying text in the label (with the text or textvariable option),
     the font option is used to specify in what font that text in the label will be displayed.
(Method 1 for font--pass a tuple e.g.font=("comicsansms",20,"bold")
Method2 for font--passing the space separated values as a string e.g. font="comicsansms 20 bold")

padx:This option is used to add extra spaces between left and right of the text within the label.The default value
     for this option is 1.

pady:This option is used to add extra spaces between top and bottom of the text within the label.The default value
     for this option is 1.
(padx and pady gives padding values from inside the label)

bd:This option is used to set the size of the border around the indicator. Default bd value is set on 2 pixels.

relief: This option is used to specify appearance of a decorative border around the label.
        The default value for this option is FLAT.values :(SUNKEN,GROOVE,RIDGE,RAISED)

justify:This option is used to define how to align multiple lines of text. Use LEFT, RIGHT, or CENTER as its values.
        Note that to position the text inside the widget, use the anchor option. Default value for justify is CENTER.

cursor:It is used to specify what cursor to show when the mouse is moved over the label.
        The default is to use the standard cursor.

underline:This

wraplength:Instead of having only one line as the label text it can be broken itno to the number of lines where
            each line has the number of characters specified to this option.


Attributes of pack
anchor: This options is used to control the positioning of the text if the widget has more space than required for
        the text. The default is anchor=CENTER, which centers the text in the available space.
Note:The values are the string literals "n", "ne", "e", "se", "s", "sw", "w", "nw", or "center".
Case is important. They represent the directions of the compass (north, south, east, and west)

side: Determines which side of the parent widget packs against:
      values(TOP,BOTTOM,RIGHT,LEFT)--It aligns the position of the widget accordingly

fill : Determines whether widget fills any extra space allocated to it by the packer, or keeps its own
minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically),
or BOTH (fill both horizontally and vertically).

padx:
pady:


'''
from tkinter import *
root=Tk()

root.geometry("444x330") #"width x height"

root.minsize(300,200) # width,height --- Sets the minimum size of the window
root.maxsize(900,700) # width,height --- Sets the maximum size of the window

root.title("MyTkinter")
text_label=Label(text='''
wraplength:Instead of having only one line as the label text it can be broken itno to \nthe number of lines where
each line has the number of characters specified to this option.
''',background="green", fg="blue" ,padx=33,pady=66,font="comicsansms 20 bold",borderwidth=10,relief=RAISED)


# text_label.pack(anchor="ne",side=BOTTOM,fill=X)
# text_label.pack(side=LEFT,fill=Y)
# text_label.pack(side=TOP,fill=BOTH)
text_label.pack(side=LEFT,fill=Y,padx=34,pady=20)

root.mainloop()