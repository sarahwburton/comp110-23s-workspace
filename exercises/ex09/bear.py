"""File to define Bear class."""


class Bear:
    """Bear class relating to bears in the river."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Self."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increase the value of the age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat (self, num_fish: int):
        """Updates the bear's hunger score so that it increases by num_fish."""
        self.hunger_score += num_fish
        return None