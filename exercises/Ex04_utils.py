"""Exercise Four - List Utils."""
__author__: str = "730316038"


# Define the function all that returns a bool indicating whether or not all the ints in the list are the same as the one given.
def all(list: list[int], integer: int) -> bool:
    """Returns a bool indicating whether or not all the ints in the list are the same as the given int."""
    list_idx: int = 0
    # While going through the list and there isn't a different number, if the indexed list item is different from the given integer, return False.
    # If the length of the list is 0, return False. 
    if len(list) == 0:
        return False
    
    while (list_idx < len(list)):
        if list[list_idx] != integer:
            return False
        else: 
            list_idx += 1
    # If the values are all the same return True. 
    return True


# Define max to return the highest value in a list of integers.
def max(input: list[int]) -> int:
    """Returns the highest value in a list of integers."""
    # Check to make sure the length of the list is at least 1.
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    # start with the max input being the first item in the list.
    max_int: int = input[0]
    # Go through the list and if an item is larger than the previous value, it becomes the max int.
    while list_idx < len(input):
        if input[list_idx] > max_int:
            max_int = input[list_idx]
        else: 
            list_idx += 1
    # Return the highest value in the list. 
    return max_int


# Define is_equal to see if all items in two lists are the same at the same indices.
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks to see if all items in two lists are the same at the same indices."""
    list1_idx: int = 0
    list2_idx: int = 0
    # If the lists are different lengths return False. 
    if len(list1) != len(list2):
        return False

    # While going through the lists, if items at the same indices are different, return False. Otherwise, return True.
    while (list1_idx < len(list1)) and (list2_idx < len(list2)):
        if list1[list1_idx] != list2[list2_idx]:
            return False
        else:
            list1_idx += 1
            list2_idx += 1
    return True 