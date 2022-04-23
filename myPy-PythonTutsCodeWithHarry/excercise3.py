#Excercise3
n=15
print("GUESS THE NUMBER GAME\n\n")


t=9
t1=t

while t:
    print("No. of guesses left: ", t)
    inp = int(input("Enter your Guess: "))
    if inp>n:
        print("NO! Original number is lesser than your guess :",inp)
    elif inp<n:
        print("NO! Original number is greater than your guess :", inp)
    elif inp==n:
        print("Congratulations!!! You Guessed it. after ",t1-t+1,"attempts")
        break
    t-=1

if t==0:
    print("Sorry!!! You lost it. Try again bro...")
