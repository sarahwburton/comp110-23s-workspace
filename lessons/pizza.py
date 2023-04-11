"""Define Pizza Class."""

class Pizza: 

    # attributes
    size: str # small or large
    toppings: int # number of toppings
    gluten_free: bool # true if gluten free, false if not
    
    def __init__(self, size_input: str, toppings_input: int, gluten_free_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gluten_free_input
        # it actually returns self back to you

    def price(self) -> float:
        """Calculate and return the cost of a pizza."""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else: 
            cost = 5.0
        # Charge 75 cents per topping
        cost += .75 * self.toppings
        # Charge a dollar if gluten free
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_toppings: int) -> None:
        """Add a certain number of toppings."""
        # Does not return anything, but modifies
        self.toppings += num_toppings
