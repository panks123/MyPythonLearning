# excercise 1
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("News24+")
root.geometry("1000x800")

texts=[]
photos=[]
for i in range(0,5):
    with open(f"{i+1}.txt") as f:
        texts.append(f.read())

    image=Image.open(f"{i+1}.png")
    # TODO:resizing the images
    image=image.resize((225,225),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

image=image=Image.open("dp.jpg")
f0=Frame(root,height=70,width=800)
f0.pack()
Label(f0,text="News24+",font="comicsansms 30 bold", fg="navy").pack()
Label(f0,text="January 12,2090",font="comicsansms 10 bold").pack()

f=Frame(root,width=900,height=200,pady=10)
Label(f,text=texts[0]).pack(side=LEFT)
Label(f,image=image,anchor="e")
f.pack(anchor="w")

f=Frame(root,width=900,height=200,pady=10)
Label(f,text=texts[1]).pack(side=LEFT)
Label(f,image=photos[1],anchor="e")
f.pack(anchor="w")

f=Frame(root,width=900,height=200,pady=10)
Label(f,text=texts[2]).pack(side=LEFT)
Label(f,image=photos[2],anchor="e")
f.pack(anchor="w")

f=Frame(root,width=900,height=200,pady=10)
Label(f,text=texts[3]).pack(side=LEFT)
Label(f,image=photos[3],anchor="e")
f.pack(anchor="w")

f=Frame(root,width=900,height=200,pady=10)
Label(f,text=texts[4]).pack(side=LEFT)
Label(f,image=photos[4],anchor="e")
f.pack(anchor="w")

root.mainloop()
