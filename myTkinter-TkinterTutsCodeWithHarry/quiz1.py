from tkinter import *
import tkinter.messagebox as tmsg


def getRatings():
    with open("ratings.txt",'a') as f:
        f.write(f"{rating_slider.get()}\n")
    tmsg.showinfo(title="Rate Us",message="Thanks for rating us.")


root=Tk()
root.geometry("600x500")
root.title("App rating")
Label(text="How much do you like our App?").pack()
rating_slider=Scale(root,from_=0,to=10,orient=HORIZONTAL)
rating_slider.set(9)
rating_slider.pack()
Button(text="Rate",bg="cyan",command=getRatings).pack()
root.mainloop()

