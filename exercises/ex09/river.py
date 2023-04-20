"""File to define River class."""
__author__: str = "730316038"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""

    day: int  # what day of the river's lifecycle you are modeling
    bears: list  # list of Bears that stores the river's bear population
    fish: list  # list of Fish that stores the river's fish population

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish): 
            self.fish.append(Fish())
        for x in range(0, num_bears): 
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages."""
        self.surviving_fish: list[Fish] = []
        self.surviving_bears: list[Bear] = []
        
        for fish in self.fish:
            if fish.age <= 3:
                self.surviving_fish.append(fish)
                
        for bear in self.bears:
            if bear.age <= 5:
                self.surviving_bears.append(bear)

        self.fish = self.surviving_bears
        self.bears = self.surviving_fish
        return None

    def bears_eating(self):
        """For each bear if there are at least 5 fish, the bear will eat 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

        return None
    
    def check_hunger(self):
        """Check hunger score of every bear in the river."""
        self.not_starving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                self.not_starving_bears.append(bear)
        return None
        
    def repopulate_fish(self):
        """Repopulate fish."""
        self.fish = self.fish + ([((len(self.fish))//2)] * 4)
        return None
    
    def repopulate_bears(self):
        """Repopulate bears."""
        self.bears = self.bears + [((len(self.bears))//2)]
        return None
    
    def view_river(self) -> None:
        """View the number of days in the river, and number of fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
    
    def remove_fish (self, amount: int):
        """Remove the amount of Fish from the River."""
        
        self.remaining_fish: list[Fish] = []
        
        
        idx: int = 0

        while idx > amount:
            self.fish.pop(idx)
            idx += 1
        return None

