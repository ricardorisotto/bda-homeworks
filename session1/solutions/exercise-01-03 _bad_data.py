


import csv

with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if (len(row) > 4):
            print(row[4])
    print(reader.line_num)      

# Instead of: with open("movies.csv", "r", newline="", encoding="utf-8") as file,
# I am using file.seek(0) to reset the file pointer to the beginning of the file after reading it once.
# This allows me to read the file again from the beginning without having to reopen it. 
    file.seek(0)
    reader = csv.reader(file)
    first_row = next(reader)
    print(first_row)

    file.seek(0)
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        print(f"row_count: {row_count}, row: {row}")
        row_count += 1
        if row_count >= 5:
            break

    print(f"Total rows: {row_count}")

    file.seek(0)
    reader = csv.reader(file)
    for row in reader:
        if "Action" in row[4]:
            print(row) 
            break
# The benefit of using the csv module is that it handles the parsing of the CSV file correctly, 
# including cases where fields contain commas or newlines. It also provides a convenient way to 
# read and write CSV files without having to manually handle the formatting. 
# 
# The limitation of using the csv module is that it may not be as efficient as manually parsing the file
# if the file is very large, as it may require more memory and processing time. Additionally, it may not
# be suitable for all types of CSV files, such as those with non-standard delimiters or
# those that require custom parsing logic.
# 
# The time complexity of using the csv module to read a CSV file as we have done is O(n), 
# where n is the number of rows in the file.
# The space complexity is O(1) as here we are processing the file row by row.   


# Exercise 2: Handling Bad Data
#
# First download the bad data dataset from: 
# https://huggingface.co/datasets/Birkbeck/movies_incomplete
# You can use the Hugging Face CLI to download the dataset:
# hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir .

print("\n\n--- Exercise 2: Handling Bad Data ---\n")

import csv

# 1. Define the categorical lists
string_columns = ['movie_id', 'title', 'director', 'country', 'language', 'production_company']
numeric_columns = ['year', 'runtime_min', 'rating_imdb', 'votes', 'revenue_musd', 'metascore']
list_columns = ['genres', 'cast_top3']

# 2. Define the Validation Functions
def validate_string(val, row_num, col_name):
    """Checks for empty or whitespace-only strings and prints an error."""
    cleaned = val.strip()
    if not cleaned:
        print(f"validate_string: Row {row_num}: Missing data for '{col_name}' (String)")
        return None
    if cleaned.lower() in ['n/a', 'na', 'null', 'none', 'unknown']:
        print(f"validate_string: Row {row_num}: Invalid or unknown data for '{col_name}' -> '{val}' (String)")
        return None
    return cleaned

def validate_numeric(val, row_num, col_name):
    """Attempts to convert to float. Missing data returns None, bad data prints an error."""
    cleaned = val.strip()
    if not cleaned:
        print(f"validate_numeric: Row {row_num}: Missing data for '{col_name}' (Numeric)")
        return None  
    try:
        return float(cleaned)
    except ValueError:
        print(f"validate_numeric: Row {row_num}: Invalid numeric data for '{col_name}' -> '{val}'")
        return None

def validate_list(val, row_num, col_name):
    """Splits strings into lists by comma."""
    cleaned = val.strip()
    if not cleaned:
        print(f"validate_list: Row {row_num}: Missing data for '{col_name}' (List)")
        return []
    return [item.strip() for item in cleaned.split(',') if item.strip()]

# 3. Main CSV Processing
with open("movies.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    
    # Read the header
    try:
        header = next(reader)
    except StopIteration:
        print("The CSV file is empty.")
        exit()
        
    expected_cols = len(header)
    
    # Create a blueprint of column types based on the header's order
    column_blueprint = []
    for col_name in header:
        if col_name in numeric_columns:
            column_blueprint.append('numeric')
        elif col_name in list_columns:
            column_blueprint.append('list')
        else:
            column_blueprint.append('string')  # Defaults to string
            
    # Iterate through the data
    for row_num, row in enumerate(reader, start=2):
        
        # Check for malformed rows
        if len(row) != expected_cols:
            print(f"!!! Row {row_num} MALFORMED: Expected {expected_cols} cols, got {len(row)}. Skipping.")
            continue
            
        # Dictionary to store the cleanly processed row
        processed_movie = {}
        
        # Validate each cell in the row using the blueprint
        for index, val in enumerate(row):
            col_name = header[index]
            col_type = column_blueprint[index]
            
            if col_type == 'numeric':
                processed_movie[col_name] = validate_numeric(val, row_num, col_name)
            elif col_type == 'list':
                processed_movie[col_name] = validate_list(val, row_num, col_name)
            else:
                processed_movie[col_name] = validate_string(val, row_num, col_name)
                
        # processed_movie now contains the fully validated data for this row.
        # You can append it to a master list here.