"""Modify the sum function using a for...in... loop."""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    for idx in range(0, len(xs)):
        sum_total += xs[idx]
    return sum_total

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