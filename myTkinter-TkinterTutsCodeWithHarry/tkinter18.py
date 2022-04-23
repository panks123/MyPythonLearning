# tkinter18---Slider

from tkinter import *
import tkinter.messagebox as tmsg


def getDollars():
    tmsg.showinfo(title="Dollar credited",message=f"We have credited ${myslider2.get()} to your account")


root=Tk()
root.geometry("600x500")
root.title("Slider")

# # for vertical slider
# myslider1=Scale(root,from_=0,to=100)
# # for horizontal slider
# myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL)
# myslider1.pack()
# myslider2.pack()


Label(text="How many dollars do you want?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=40)  #tickinterval divides the slider in intervals and shows the value below
myslider2.set(50)  # It sets the initial pointer of the slider
myslider2.pack()
Button(text="Get Dollars",command=getDollars).pack()
root.mainloop()