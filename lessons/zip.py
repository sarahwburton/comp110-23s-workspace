"""Challenge Question 4."""

def zip (keys: list[str], values: list[int]) -> dict[str, int]:
    """Return a dictionary where the keys are the list of the first string, and the values are the list of the second string."""
   
    dictionary: dict[str, int] = dict()
   
    if len(keys) != len(values):
        return dictionary
    
    if (len(keys) or len(values)) == 0:
        return dictionary
    
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]

    return dictionary