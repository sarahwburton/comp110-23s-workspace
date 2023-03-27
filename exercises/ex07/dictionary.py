"""Exercise Seven - Dictionary Functions """
__author__: str = "730316038"

def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Make the keys of a given list the values, and values the keys in a new list."""
    new_dictionary: dict[str, str] = {}
    
    for key in dictionary:
         val = dictionary[key]
         new_dictionary[val] = key
    
    return new_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """Return the most frequently reported color."""
    colors: list(str) = list(dictionary.values())
    color: str = colors[0]
    highest_frequency: int = 0

    for i in colors:
        item_frequency: int = colors.count(i)
        if (item_frequency > highest_frequency):
            highest_frequency = item_frequency
            color = i
    
    return color


def count(items: list[str]) -> dict[str, int]:
    """Create a dictionary reporting the frequencies of items in a list."""
    frequency_dictionary: dict[str, int] = {}

    for i in items:
        if i in frequency_dictionary:
            frequency_dictionary[i] += 1
        else: 
            frequency_dictionary[i] = 1
    return frequency_dictionary


          
        
    




