# Guess The number
# Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum number of trials wins!
#
# Randomly generate a number after taking a and b as input and don’t show that to the user (say 6)
#
# Input:
#
# Enter the value of a
#
# 4
#
# Enter the value of b
#
# 13
#
# Output:
#
# Player1 :
#
# Please guess the number between 4 and 13
#
# 5
#
# Wrong guess a greater number again
#
# 8
#
# Wrong guess a smaller number again
#
# 6
#
# Correct you took 3 trials to guess the number
#
# Player 2:
#
# .
#
# .
#
# .
#
# Correct you took 7 trials to guess the number
#
# Player 1 wins!

from random import  randint

print("Enter two numbers")
a=int(input())
b=int(input())

num=randint(a,b)

print(f"Player 1 chance: Guess the number between {a} and {b}\n")
player1_count=1
while True:
    guess=int(input())
    if guess<num:
        print("Your guess is smaller than the actual number   Try a greater value \nGuess again...\n")
    elif guess>num:
        print("Your guess is greater than the actual number   Try a lesser value\nGuess again...\n")
    else:
        print(f"Congratulations! You guessed it in {player1_count} attempts\n\n")
        break
    player1_count+=1


num=randint(a,b)

print(f"Player 2 chance: Guess the number between {a} and {b}\n")
player2_count=1
while True:
    guess=int(input())
    if guess<num:
        print("Your guess is smaller than the actual number   Try a greater value \nGuess again...\n")
    elif guess>num:
        print("Your guess is greater than the actual number   Try a lesser value\nGuess again...\n")
    else:
        print(f"Congratulations! You guessed it in {player1_count} attempts\n\n")
        break
    player2_count += 1

print(f"Comparison:  (Player1: {player1_count} attempts) | Player2: {player2_count} attempts)")
if player1_count<player2_count:
    print("Player1 Won")
elif player2_count<player1_count:
    print("Player2 Won")
else:
    print("It is a tie")


