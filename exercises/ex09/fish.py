"""File to define Fish class"""


class Fish:
    """Fish class relating to fish in the river."""
    age: int

    def __init__(self):
        """Self."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increase the value of the age attribute by 1."""
        self.age += 1
        return None