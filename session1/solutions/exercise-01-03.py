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


import csv

# 1. Define the categorical lists
string_columns = ['movie_id', 'title', 'director', 'country', 'language', 'production_company']
numeric_columns = ['year', 'runtime_min', 'rating_imdb', 'votes', 'revenue_musd', 'metascore']
list_columns = ['genres', 'cast_top3']

# 2. Define the Cleaning Function
def clean_string(val):
    """Only removes leading/trailing whitespace. Does not judge or alter the core data."""
    return val.strip()


# 3. Define the Validation Functions (These assume the data is already cleaned)
def validate_string(cleaned_val, row_num, col_name):
    """Checks for empty strings or known missing indicators explicitly."""
    missing_indicators = ['n/a', 'na', 'null', 'none', '']
    
    if cleaned_val.lower() in missing_indicators:
        print(f"Row {row_num}: Invalid or missing data for '{col_name}' (String)")
        return None
        
    return cleaned_val

def validate_numeric(cleaned_val, row_num, col_name):
    """Attempts to convert to float. Explicitly checks for missing data indicators."""
    missing_indicators = ['n/a', 'na', 'null', 'none', '']
    
    if cleaned_val.lower() in missing_indicators:
        print(f"Row {row_num}: Invalid or missing data for '{col_name}' (Numeric)")
        return None
        
    try:
        return float(cleaned_val)
    except ValueError:
        print(f"Row {row_num}: Invalid numeric data for '{col_name}' -> '{cleaned_val}'")
        return None

def validate_list(cleaned_val, row_num, col_name):
    """Splits strings into lists by comma. Explicitly checks for missing data indicators."""
    missing_indicators = ['n/a', 'na', 'null', 'none', '']
    
    if cleaned_val.lower() in missing_indicators:
        print(f"Row {row_num}: Invalid or missing data for '{col_name}' (List)")
        return []
        
    # We still need to strip individual items within the list after splitting
    return [item.strip() for item in cleaned_val.split(',') if item.strip()]


# 4. Main CSV Processing Pipeline
with open("movies.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    
    # Read the header safely
    try:
        header = next(reader)
    except StopIteration:
        print("The CSV file is empty.")
        exit()
        
    expected_cols = len(header)
    
    # Create a blueprint of column types based on the header's exact order
    column_blueprint = []
    for col_name in header:
        if col_name in numeric_columns:
            column_blueprint.append('numeric')
        elif col_name in list_columns:
            column_blueprint.append('list')
        else:
            column_blueprint.append('string')  # Fail-safe: Defaults unknown columns to string
            
    # List to hold all the fully validated dictionaries
    valid_movies = []
            
    # Iterate through the data rows
    for row_num, row in enumerate(reader, start=2):
        
        # Check for malformed rows (wrong number of columns)
        if len(row) != expected_cols:
            print(f"!!! Row {row_num} MALFORMED: Expected {expected_cols} cols, got {len(row)}. Skipping.")
            continue
            
        processed_movie = {}
        
        # Process each cell in the row
        for index, val in enumerate(row):
            col_name = header[index]
            col_type = column_blueprint[index]
            
            # Step 1: Clean (remove whitespace)
            cleaned_val = clean_string(val)
            
            # Step 2: Validate & Parse
            if col_type == 'numeric':
                processed_movie[col_name] = validate_numeric(cleaned_val, row_num, col_name)
            elif col_type == 'list':
                processed_movie[col_name] = validate_list(cleaned_val, row_num, col_name)
            else:
                processed_movie[col_name] = validate_string(cleaned_val, row_num, col_name)
                
        # Step 3: Store the clean, validated row
        valid_movies.append(processed_movie)

# Optional: Print success message
print(f"\nProcessing complete. Successfully validated {len(valid_movies)} rows.")