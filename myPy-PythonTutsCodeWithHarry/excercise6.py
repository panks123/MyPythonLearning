#excercise6-Snake water Gun

import random


list1=["Snake","Water","Gun"]
comptr_win=0
you_win=0
t=10
while(t):
    inp=input("Choices: \ns: Snake w: Water g: Gun\nEnter s/w/g")
    if inp=="s" or inp=="w" or inp=="g":


        comptr_choice=random.choice(list1)
        if (inp=="s" and comptr_choice=="Snake") or(inp=="w" and comptr_choice=="Water") or (inp=="g" and comptr_choice=="Gun"):
            print("No one won...")
        else:
            if inp=="s" and comptr_choice=="Water":
                print("You won")
                you_win+=1
            elif inp=="w" and comptr_choice=="Snake":
                print("Your opponent won")
                comptr_win+=1
            elif inp=="s" and comptr_choice=="Gun":
                print("Your opponent won")
                comptr_win+=1
            elif inp=="g" and comptr_choice=="Snake":
                print("You won")
                you_win+=1
            elif inp=="w" and comptr_choice=="Gun":
                print("You won")
                you_win+=1
            else:
                print("Your opponent won")
                comptr_win+=1
    t=t-1
print("You score :",you_win,"  Your opponent's score :",comptr_win)
print("You won the game") if you_win>=comptr_win else print("Your opponent won the game")
print("\n\nGame over!!! Play again...")
