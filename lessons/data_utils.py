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

def column_vals(table: list[dict[str, str]], header: str) -> list[str, str]:
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
        result[key] = column_vals(table, key)
    return result
