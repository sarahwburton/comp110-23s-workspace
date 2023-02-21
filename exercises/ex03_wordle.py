"""Exercise Three - Wordle."""
__author__: str = "730316038"

#Define a function contains_char that when given two strings, the first of any length, and the second a single character will return True if the single character of the second string is found at any index of the first string, and return false otherwise

def contains_char (string: str, character:str) -> bool:
    """Returns True if the character given is at any index in the given string."""
    assert len(character) == 1
    str_idx: int = 0
    contains: bool = False
    while (str_idx < len(string)) and (contains == False):
        if string[str_idx] == character:
            contains = True
        else:
            str_idx = str_idx + 1
    return contains
        

def emojified (guess: str, secret: str) -> str:
    """Given two strings of equal length, will return emojis indicating correctness of guess correlated to secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    guess_idx: int = 0
    guess_emoji: str = ""

    while guess_idx < len(guess):
        if guess[guess_idx] == secret[guess_idx]:
            guess_emoji = guess_emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[guess_idx]) == True:
                guess_emoji = guess_emoji + YELLOW_BOX
            else: 
               guess_emoji = guess_emoji + WHITE_BOX 
        guess_idx = guess_idx + 1
    return guess_emoji
            
def input_guess (expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    has_won: bool = False
    
    while (turns <= 6) and (has_won == False):
        print (f"=== Turn {turns}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            has_won = True
        else:
            turns = turns + 1
    
    if has_won == True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, tray again tomorrow!")

if __name__ == "__main__":
    main()