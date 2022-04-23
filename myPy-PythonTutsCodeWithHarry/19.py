# excercise 5

def getdate():
    import datetime
    return datetime.datetime.now()

def LogMyFoodorExcercise(name):
    if name==1:
        option=int(input("Select option:\n1. Log Food\n2. Log Exercise"))
        if option==1:
            i=input("Enter (Kya khaya): ")
            with open("Harry_food.txt","a") as f:
                f.write("["+str(getdate())+"] : "+i+"\n")

        elif option == 2:
            i = input("Enter (Kya excercise kiya): ")
            with open("Harry_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : "+i+"\n")
        else:
            print("Invalid input")
            return

    elif name==2:
        option = int(input("Select option:\n1. Log Food\n2. Log Exercise"))
        if option==1:
            i=input("Enter (Kya khaya): ")

            with open("Rohan_food.txt","a") as f:
                f.write("["+str(getdate())+"] : "+i+"\n")

        elif option == 2:
            i = input("Enter (Kya excercise kiya): ")
            with open("Rohan_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : "+i+"\n")
        else:
            print("Invalid input")
            return

    elif name==3:
        option = int(input("Select option:\n1. Log Food\n2. Log Exercise"))
        if option==1:
            i=input("Enter (Kya khaya): ")
            with open("Hamad_food.txt","a") as f:
                f.write("["+str(getdate())+"] : "+i+"\n")

        elif option == 2:
            i = input("Enter (Kya excercise kiya): ")
            with open("Hamad_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : "+i+"\n")
        else:
            print("Invalid input")
            return

    else:
        print("Invalid input")
        return
    print("Successfully Logged your data")

def retrieve_data(name):
    if name==1:
        option = int(input("Select option:\n1. Retrieve Food\n2. Retrieve Exercise"))
        if option==1:
            with open("Harry_food.txt") as f:
                print(f.read())
        elif option==2:
            with open("Harry_ex.txt") as f:
                print(f.read())

        else:
            print("Invalid input")
            return

    elif name==2:
        option = int(input("Select option:\n1. Retrieve Food\n2. Retrieve Exercise"))
        if option==1:
            with open("Rohan_food.txt") as f:
                print(f.read())
        elif option==2:
            with open("Rohan_ex.txt") as f:
                print(f.read())

        else:
            print("Invalid input")
            return

    elif name==3:
        option = int(input("Select option:\n1. Retrieve Food\n2. Retrieve Exercise"))
        if option==1:
            with open("Hamad_food.txt") as f:
                print(f.read())
        elif option==2:
            with open("Hamad_ex.txt") as f:
                print(f.read())
        else:
            print("Invalid input")
            return
    else:
        print("Invalid input")
        return

print("Select your option: \n1. Log data\n2.Retrieve data\n")

inp=int(input())
if inp ==1:
    name=int(input("Who are you: 1.Harry 2. Rohan 3. Hamad\n(Enter 1/2/3)"))
    LogMyFoodorExcercise(name)
elif inp==2:
    name = int(input("Who are you: 1.Harry 2. Rohan 3. Hamad\n(Enter 1/2/3)"))
    retrieve_data(name)

else:
    print("Invalid input!!!")



