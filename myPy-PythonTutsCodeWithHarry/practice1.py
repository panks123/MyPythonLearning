# Python Practice problem 1 (Easy, 10 points)
# Your Age In 2090
# Take age or year or birth as an input from the user and tell them when they will turn 100 years old.(5 points)
# Don’t use any type of module like datetime or dateutils(-5 points).
#
# They can then optionally provide a year and your program must tell their age in that particular year. (3 points)
# You should be handling all sorts of errors like (2 points):
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other error if possible!


try:
    cy=int(input("Enter current year"))
    if cy<1900 or cy>3000:
        print("Invalid year")
        exit()
    inp=int(input("Enter your age or year of birth: "))
except Exception as e:
    print("Enter a valid input(Current year and Your age or birth year should be in number)   Try again...")
    exit()
if inp>1900 and inp<5000:
    print("You entered your birth yr")
    birth_year = inp
    if birth_year>cy:
        print("You are yet to be born.  Sorry!!!")
        exit()


elif inp>0 and inp<150:
    print("You entered your age")
    if inp>120:
        print("Congratulations!!! You are the oldest person alive \n"
              "Sorry! We can't service you. We can only salute you ")
        exit()
    else:
        age=inp
        birth_year=cy-age
        print(birth_year)
else:
    print("Sorry!! Check your input")
    exit()
if(2090>birth_year):
    print("Your age in 2090 will be :",2090-birth_year)

print(f"you will be 100 years old in {birth_year+100}")

inputyr=input("Do you want to know your age in a particular year(Enter \"YES\" or \"NO\"): ")
if inputyr=="Yes" or inputyr =="YES" or inputyr=="yes":
    try:
        yr=int(input("Enter year: "))
    except Exception as e:
        print("Not a valid input  Sorry!!!")
        exit()
    if(yr>birth_year):
        print("Your age in ",yr,"Will be : ",yr-birth_year)
    else:
        print("Not a suitable year")

elif inputyr=="No" or inputyr =="NO" or inputyr=="no":
    print("Thank You!!! Visit again...")
else:
    print("Invalid input")
