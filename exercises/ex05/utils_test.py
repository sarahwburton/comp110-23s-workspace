"""Exercise Five - List Utility Functions Tests."""
__author__: str = "730316038"

# Import functions.
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

# Create tests to make sure that only_evens works at different conditions.


def test_all_even() -> None:
    """Ensure all even numbers are returned when given all even numbers."""
    test_list: list[int] = [2, 4, 6, 8]
    assert only_evens(test_list) == [2, 4, 6, 8]


def test_mixed_numbers() -> None: 
    """Ensure all even numbers are returned when there is a mix of even and odd numbers."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_empty_list() -> None:
    """Ensure an empty list is returned when an empty list is given as the argument."""
    test_list: list[int] = list()
    assert only_evens(test_list) == []


def test_all_evens() -> None:
    """Ensure an empty list is returned when a list of all even numbers are given as the argument."""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == []


# Create tests to make sure that sub works at different conditions.


def test_sub_empty() -> None:
    """Ensure an empty list is returned when the length of the list is 0."""
    test_list: list[int] = list()
    assert sub(test_list, 1, 3) == []


def test_sub_wide_range() -> None:
    """Ensure the sub function works with a wide range."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert sub(test_list, 1, 9) == [2, 3, 4, 5, 6, 7, 8, 9]


def test_sub_narrow_range() -> None:
    """Ensure the sub function works with a narrow range."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert sub(test_list, 1, 2) == [2]


# Create tests to ensure the concat function works with different conditions.


def test_concat_empty_lists() -> None:
    """Ensure the concat function returns an empty list when two empty lists are given."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_concat_two_lists_same_length() -> None:
    """Ensure the concat function combines two lists of the same length."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_concat_two_lists_different_length() -> None:
    """Ensure the concat function combines two lists of different lengths."""
    test_list1: list[int] = [1, 2, 3, 4]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]