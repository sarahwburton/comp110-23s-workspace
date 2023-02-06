"""Asks for a number, goes until they get it right"""

#Often constants are noted with all caps, since 4 is the secret number it won't change
SECRET: int = 4

guess: int = int(input("Guess a number! "))

#You want the program to keep running until they guess the right number

playing: bool = True

# While True...what will happen?

number_of_guesses: int = 0

while playing:
    if number_of_guesses == 3:
        playing = False
    if guess == SECRET:
        print("Yay! You got it right!")
        playing = False
    else: 
        print("Wrong number. :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd. The answer is even.")
        if guess > SECRET: 
            print("Your guess is too high! ")
        else: #guess<secret
            print("Your guess is too low!")
        guess = int (input("Make another guess! "))
number_of_guesses = number_of_guesses + 1
print("Number of guesses: " + number_of_guesses)



