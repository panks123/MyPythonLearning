# tkinter 1--- Widgets and Attributes

# GUI is the collection of packed widgets

# Widgets---- in Tkinter are the elements of GUI application which provides various controls 
# (such as Labels, Buttons, ComboBoxes, CheckBoxes, MenuBars, RadioButtons and many more) 
# to users to interact with the application.

'''
                       Fundamental steps of a Tkinter Program
                       1. Importing Tkinter modules
                       2. Creating the main window for the GUI app
                       3. Adding widgets to the app
                       4. Enter the main event loop

Label---	It is used to display text or image on the screen
Button--- 	It is used to add buttons to your application
Canvas--- 	It is used to draw pictures and others layouts like texts, graphics etc.
ComboBox--- 	It contains a down arrow to select from list of available options
CheckButton--- 	It displays a number of options to the user as toggle buttons from which user can select any number of options.
RadioButton--- 	It is used to implement one-of-many selection as it allows only one option to be selected
Entry--- 	It is used to input single line text entry from user
Frame--- 	It is used as container to hold and organize the widgets
Message--- 	It works same as that of label and refers to multi-line and non-editable text
Scale--- 	It is used to provide a graphical slider which allows to select any value from that scale
Scrollbar--- 	It is used to scroll down the contents. It provides a slide controller.
SpinBox--- 	It is allows user to select from given set of values
Text--- 	It allows user to edit multiline text and format the way it has to be displayed
Menu--- 	It is used to create all kinds of menu used by an application--- 

'''

# Displaying images using Label widget
from tkinter import *
from PIL import  Image,ImageTk   #for  jpg images

root=Tk()
root.title("MyTKINTER")  #Sets the title of The GUI
root.geometry("455x520")    #It sets the geometry of the GUI window
photo=PhotoImage(file='python.png') #It loads the image --Tkinter does not supports jpg images
label=Label(image=photo)  # creates the label widget containing image

#for  jpg images
image=Image.open("dp.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()


root.mainloop()

