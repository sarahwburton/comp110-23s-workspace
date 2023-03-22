"""Practice with dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# To add an element
ice_cream["mint"] = 3

print("After adding mint:")
print(ice_cream)

# To remove an element
ice_cream.pop("mint")

print("After removing mint:")
print(ice_cream)

# Accessing an item
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# Modifying an item
ice_cream["vanilla"] += 1
print("After adding 1 vanilla: ")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)