# if-elif-else

inp_age=int(input("Enter your age"))
if inp_age<7:
    print("Abhi tu maa ka doodh pee bachhe")
elif inp_age>7 and inp_age<18:
    print("You cannot drive")
elif inp_age==18:
    print("We'll think about you")
elif(inp_age>18 and inp_age<100):
    print("You can drive")
else:
    print("I salute you for being 100+")