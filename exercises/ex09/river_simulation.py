from exercises.ex09.river import River

my_river: River = River(10, 2)
my_river.view_river()





# fish_list: list[str] = ["fish one", "fish two", "fish three", "fish four", "fish five", "fish six"]


def remove_fish (input_list: list[str], amount: int):
    """Remove the amount of Fish from the River."""
    idx: int = 0
    removed_fish: list[str] = []

    while idx > amount:
        input_list -= input_list[idx]
        idx += 1
    return None
