from csv import DictReader

def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(file_name, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
  
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar (table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that its a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    #Loop through keys of one row of a table to get keys
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # Assign value as a list of the column values (using column_vals)
        result[key] = column_values(table, key)
    return result


def head (input_dict: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce new column-based table with only the first N rows of data for each column."""
    
    result_dict: dict[str, list[str]] = {}

    for key in input_dict:
        first_values: list[str] = []
        idx: int = 0
        for values in input_dict[key]:
            if idx < N:
                first_values.append(values)
                idx += 1
        result_dict[key] = first_values
    return result_dict


def select (input_dict: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of columns."""
    result_dict: dict[str, list[str]] = {}

    for column in column_names:
        result_dict[column] = input_dict[column]
    return result_dict


def concat (table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result_dict: dict[str, list[str]] = {}

    for key in table_one:
        result_dict[key] = table_one[key]
        
    for key in table_two:
        if key in result_dict:
            result_dict[key] += table_two[key]
        else:
            result_dict[key] = table_two[key]
    return result_dict


def count (values: list[str]) -> dict[str, int]:
    """Produce a dict where each key is a unique value in a list, and each value is the count of the number of times that value appeared in the list."""
    result_dict: dict[str, int] = {}

    for item in values:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict
