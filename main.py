"""
OpritzaMonegan
GuessTheNumber

"""
# My guess the number game
print ("Let's play Guess The Number!")
print ("Try to get the least amount of guesses as possible")

# Level 1 is the first level of the game. It lets you have 5 guesses and if you get them all wrong, the game moves you on to the next level.
print ("Level 1")
import random
random_number = random.randint(1,10)
win = False
Turns =0
while win==False and Turns <= 4:
    Your_guess = input("Enter a number between 1 and 10: ")
    Turns +=1
    if random_number==int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your guess was too low, try again.")
     else:
        print("Your guess was too high, try again.")
    if Turns > 4:
      print("Oh no! You ran out of guesses! Time for the next level")

# Level 2 is the second level of the game. It lets you have 10 guesses and if you get them all wrong, the game moves you onto the next level.
print ("Level 2")
import random
random_number = random.randint(1,50)
win = False
Turns =0
while win==False and Turns <= 9:
    Your_guess = input("Enter a number between 1 and 50: ")
    Turns +=1
    if random_number==int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your guess was too low, try again.")
     else:
        print("Your guess was too high, try again.")
    if Turns > 9:
      print("Oh no! You ran out of guesses! Time for the next level")

# Level 3 is the third level of the game. It lets you have 15 guesses and if you get them all wrong, the game ends.
print ("Level 3")
import random
random_number = random.randint(1,100)
win = False
Turns =0
while win==False and Turns <= 14:
    Your_guess = input("Enter a number between 1 and 100: ")
    Turns +=1
    if random_number==int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your guess was too low, try again.")
     else:
        print("Your guess was too high, try again.")
# The end of the game just tells you whether or not you won or lost. If you passed 2/3 of the levels, then that means that you won.
print("If you passed 2/3 of the levels with the right amount of guess, then you win! If not, you lose.")