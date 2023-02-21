"""Exercise Two - One Shot Wordle."""
__author__: str = "730316038"

secret_word: str = "python"

number_of_characters: int = len(secret_word)

guess: str = input(f"What is your {number_of_characters}-letter guess? ")

playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# going through the characters in the guess
guess_idx: int = 0
guess_emoji: str = ""


while playing:
    # if the length of the guess is not the same as the length of the secet word, ask to try again
    if len(guess) != number_of_characters:
        guess = input(f"That was not {number_of_characters} letters! Try again: ")
    # choosing which color box to print, if the same print green, if not in the word print white, if somewhere else print yellow
    else: 
        while guess_idx < number_of_characters:
            if guess[guess_idx] == secret_word[guess_idx]:
                guess_emoji = guess_emoji + GREEN_BOX
            else:
                anywhere_else: bool = False
                secret_idx: int = 0
                while (anywhere_else is False) and (secret_idx < number_of_characters):
                    if secret_word[secret_idx] == guess[guess_idx]:
                        anywhere_else = True
                    else:
                        secret_idx = secret_idx + 1
                if anywhere_else is True:
                    guess_emoji = guess_emoji + YELLOW_BOX
                else: 
                    guess_emoji = guess_emoji + WHITE_BOX
            guess_idx = guess_idx + 1
        print(guess_emoji)
        # if the word is guessed right
        if guess == secret_word:
            print("Woo! You got it!")
            playing = False
        # if the word is not guessed right
        if (guess != secret_word) and (len(guess) == number_of_characters):
            print("Not quite. Play again soon!")
            playing = False
