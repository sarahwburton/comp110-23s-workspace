"""Randomly rolls dice and sums total."""

from random import randint

roll1: int = randint(1,6)
roll2: int = randint(1,6)
roll3: int = randint(1,6)

#Make a list of the two values stored when you roll the dice
dice_rolls: list[int] = [roll1, roll2, roll3]

#Make a while loop to look at every element in the list and print it in list form

dice_idx: int = 0
dice_sum: int = 0

while dice_idx <= len(dice_rolls) - 1:
    print(dice_rolls[dice_idx])
    dice_sum += dice_rolls[dice_idx]
    dice_idx += 1
print(dice_sum)

#Use dice sum to add together the value of the rolled dice in the list