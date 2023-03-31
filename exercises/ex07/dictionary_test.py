"""Exercise Six - Choose Your Own Adventure."""
__author__: str = "730316038"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

# INVERT TESTS.


def test_invert_with_empty_list() -> None:
    """Ensure an empty dictionary is returned when an empty dictionary is given."""
    test_dictionary: dict[str, str] = {}
    assert invert(test_dictionary) == {}


def test_invert_single_letter() -> None:
    """Ensure single characters are swapped from keys to values in new dict."""
    test_dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_full_words() -> None:
    """Ensure full words of strings are swapped from keys to values in new dict."""
    test_dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(test_dictionary) == {'cat': 'apple'}


# FAVORITE COLOR TESTS.


def test_fav_color_tie() -> None:
    """Ensure that if there is a tie for most frequently reported color, the first one that appeared in the list is given."""
    test_dictionary: dict[str, str] = {"Marc": "yellow", "Sarah": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dictionary) == "yellow"


def test_fav_color_many() -> None:
    """Ensure that the most frequently reported color is given."""
    test_dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dictionary) == "blue"


def test_fav_color_one_item() -> None:
    """Ensure a color is returned when it is the only one given."""
    test_dictionary: dict[str, str] = {"Marc": "blue"}
    assert favorite_color(test_dictionary) == "blue"
    

# COUNT TESTS.


def test_count_multiple_items() -> None:
    """Ensure the frequencies of multiple items in a list are returned."""
    test_list: list[str] = ('blue', 'blue', 'yellow', 'yellow', 'pink', 'pink')
    assert count(test_list) == {'blue': 2, 'yellow': 2, 'pink': 2}


def test_count_one_item_multiple_times() -> None:
    """Ensure one element is returned with the correct number of counts."""
    test_list: list[str] = ('blue', 'blue', 'blue', 'blue', 'blue',)
    assert count(test_list) == {'blue': 5}


def test_count_empty() -> None:
    """Ensure an empty list is returned when no items are added to a list."""
    new_list: list[str] = []
    assert count(new_list) == {}
