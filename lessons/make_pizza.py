"""Practice Instantiating Pizza Class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)

# def price(pizza_order: Pizza) -> float:
#     """Calculate and return the cost of a pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else: 
#         cost = 5.0
#     # Charge 75 cents per topping
#     cost += .75 * pizza_order.toppings
#     # Charge a dollar if gluten free
#     if pizza_order.gluten_free:
#         cost += 1.00
#     return cost

# Original number of toppings and price
print(my_pizza.toppings)
print(my_pizza.price())

# New number of toppings and new price
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())
