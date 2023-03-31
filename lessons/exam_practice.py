def odd_and_even(list_input: list[int]) -> list[int]:
    
    odd_values: list[int] = list()
    
    for item in range(1, len(list_input), step = 2):
        odd_values.append(f"{list_input[item]}")
    
    
    return print(odd_values)

