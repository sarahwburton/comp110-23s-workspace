import random


player: str = ""
points: int = 0

SAD_FACE: str = "\U0001F614"
CONGRATULATIONS: str = "\U0001F389"
WAVE: str = "\U0001F44B"


def greet() -> None:
   global player
   player = input("Welcome to the guessing game! What is your name? ")


def guess_color() -> None:
    global player
    global points
    
    # List of colors, pick random card color as the mystery color being guessed.
    colors: list(str) = ['red', 'black']
    card_color: str = random.choice(colors)
    
    # Have the player guess the color of the mystery card, make sure it is either red or black.
    color_guess: str = input(f"{player}, do you think the card I draw will be red or black? ")
    assert (color_guess == "red") or (color_guess == "black")

    # Print the chosen color
    print(f"The card chosen was {card_color}")

    # See if they guessed correctly and assign points
    if color_guess == card_color:
        print(f"You guessed correctly, {player}! {CONGRATULATIONS}")
        points += 1
    else: 
        print(f"You did not guess correctly {SAD_FACE}, better luck next time!")
    

def guess_suit(player_points: int) -> int:
    global player

    # List of suits, pick random card suit as the mystery suit being guessed.
    suits: list(str) = ['hearts', 'diamonds', 'clubs', 'spades']
    card_suit: str = random.choice(suits)
    
    # Have the player guess the suit of the mystery card, make sure it is one of the four options.
    suit_guess: str = input(f"{player}, do you think the card I draw will be hearts, diamonds, spades, or clubs? ")
    assert (suit_guess == "hearts") or (suit_guess == "diamonds") or (suit_guess == "clubs") or (suit_guess == "spades")

    # Print the chosen suit
    print(f"The card chosen was {card_suit}")

    # See if they guessed correctly and assign points
    if suit_guess == card_suit:
        print(f"You guessed correctly, {player}! {CONGRATULATIONS}")
        player_points += 1
    else: 
        print(f"You did not guess correctly {SAD_FACE}, better luck next time!")

    return player_points
    
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    global points
    # Greet the player and get their name saved as player. 
    greet()
    
    playing: bool = True

    while playing is True:
        print(f"{player}, you currently have {points} points.")
    
        print(f"{player}, you have three choices. You can attempt to guess the color of my mystery card, the suit of my mystery card, or quit the game now. ")
        print("To attempt to guess the color, choose A.")
        print("To attempt to guess the suit, choose B.")
        print("To quit the game, choose C.")
        
        path: str = input(f"{player}, which path do you choose? ")
        assert (path == "A") or (path == "B") or (path == "C")

        #Chooses to guess the color.
        if path == "A":
            guess_color()

        #Chooses to guess the suit.
        if path == "B":
            points += guess_suit(points)
            
        if path == "C":
            print(f"See you next time, {player}! {WAVE}")
            playing = False

    
if __name__ == "__main__":
    main()