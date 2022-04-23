'''
Creting a form and using checkbuttons and entry widget and storing the user's input in a file
'''
from tkinter import *

def getValues():
    print(f"Name:{name_val.get()} phone:{phone_val.get()} gender:{gender_val.get()} Emergency Contact: "
          f"{emergency_val.get()} payment mode: {payment_mode_val.get()} food service: {foodservice_val.get()}")
    with open("records.txt",'a') as f:
        f.write(f"{name_val.get(),phone_val.get(),gender_val.get(),emergency_val.get(),payment_mode_val.get(),foodservice_val.get()}\n")
    
    

root=Tk()
root.geometry("540x320")
root.title("Travel form")

# heading
Label(text="Welcome to ABC Travels",font="comicsansms 18 bold",pady=15).grid(row=0,column=3)

# text for the form
name=Label(root,text="Name: ",pady=3,font="comicsansms 8 bold")
phone=Label(root,text="Phone: ",pady=3,font="comicsansms 8 bold")
gender=Label(root,text="Gender: ",pady=3,font="comicsansms 8 bold")
emergency=Label(root,text="Emergency Contact: ",pady=3,font="comicsansms 8 bold")
payment_mode=Label(root,text="Payment Mode: ",pady=3,font="comicsansms 8 bold")

# packing texts of the form using grid layout
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment_mode.grid(row=5,column=2)

# tkinter variables for storing values of entries
name_val=StringVar()
phone_val=StringVar()
gender_val=StringVar()
emergency_val=StringVar()
payment_mode_val=StringVar()
foodservice_val=IntVar()

# entries
name_entry=Entry(root,textvariable=name_val)
phone_entry=Entry(root,textvariable=phone_val)
gender_entry=Entry(root,textvariable=gender_val)
emergency_entry=Entry(root,textvariable=emergency_val)
payment_mode_entry=Entry(root,textvariable=payment_mode_val)

# packing entries using grid
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
emergency_entry.grid(row=4,column=3)
payment_mode_entry.grid(row=5,column=3)

# checkbox and packing it
foodservice=Checkbutton(text="Want to pre-book your food?",font="comicsansms 10 bold",variable=foodservice_val)
foodservice.grid(row=6,column=3)

# creting a submit button and packing it using grid and assigning it a command
btn=Button(text="Submit",bg="cyan",fg="blue",command=getValues)
btn.grid(row=7,column=2)

root.mainloop()