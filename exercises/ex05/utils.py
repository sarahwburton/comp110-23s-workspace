"""Exercise Five - List Utility Functions."""
__author__: str = "730316038"

# Only_evens should take a list of ints and return a new list containing only the even elements of the list.

def only_evens (numbers: list[int]) -> list[int]:
    new_list: list[int] = list()
    for item in numbers:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


# Concat will combine two lists. 
def concat (list1: list[int], list2: list[int]) -> list[int]:
    new_list: list[int] = list()
    new_list += list1
    new_list += list2
    return new_list 

# Sub will return a range within the given list based on the start and end idxs.
def sub (numbers: list[int], start_idx: int, end_idx: int):
    new_list: list[int] = list()
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(numbers):
        end_idx = len(numbers) 
    if len(numbers) == 0:
        return numbers
    if start_idx >= len(numbers):
        return []
    if end_idx <= 0:
        return []
    for idx in range(start_idx, end_idx):
        new_list.append(numbers[idx])
    return new_list

print(sub([10, 20, 30, 40, 50], 1, 3))