"""Unit tests for sum function."""
# To test the sum function you have to import it
from lessons.sum import sum

# Create a test to make sure that it works at different conditions
def test_empty() -> None:
    assert sum([]) == 0.0

def test_one_element() -> None:
    test_list: list[float] = [1.0]
    assert sum(test_list) == 1.0

def test_many() -> None: 
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert sum(test_list) == 6.0

def test_many_with_negatives() -> None:
    test_list: list[float] = [1.0, -2.0, 1.0]
    assert sum(test_list) == 0.0
    