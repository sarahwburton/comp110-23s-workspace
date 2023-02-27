"""Exercise Four - List Utils."""
__author__: str = "730316038"

def all (list: list[int], integer: int) -> bool:
    """Returns a bool indicating whether or not all the ints in the list are the same as the given int."""
    list_idx: int = 0
    something_different: bool = False
    while (list_idx < len(list)) and (something_different == False):
        if list[list_idx] != integer:
            something_different = True
        else: 
            list_idx += 1
    return not(something_different)

def max (input: list[int]) -> int:
    """Returns the highest value in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    max_int: int = 0
    while list_idx < len(input):
        if input[list_idx] > max_int:
            max_int = input[list_idx]
        else: 
            list_idx += 1
    return max_int

def is_equal (list1: list[int], list2: list[int]) -> bool:
    list1_idx: int = 0
    list2_idx: int = 0
    same: bool = True
    while (list1_idx < len(list1)) and (list2_idx < len(list2)) and (same == True):
        if list1[list1_idx] != list2[list2_idx]:
            same = False
        else:
            list1_idx += 1
            list2_idx += 1
    return same

print(is_equal([1, 2, 0], [1, 2, 0]))