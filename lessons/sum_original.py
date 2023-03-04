"""Example function for unit tests."""

def sum1(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum_total

# Created the function, test to make sure it works correctly.
# To test, the file has to have .py at the end of the file name. 