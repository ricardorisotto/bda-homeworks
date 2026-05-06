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

    # Flag to track if we've found the first Action movie
    is_action_movie_found = False
            
    # Iterate through the data rows
    for row_num, row in enumerate(reader, start=2):

        # Print first 3 rowws
        if row_num == 2:
            print(f"Printing first 3 data rows:\n")
        if row_num <= 4:  
            print(f"Row {row_num}: {row}")

        

        # Check for malformed rows (wrong number of columns)
        if len(row) != expected_cols:
            print(f"!!! Row {row_num} MALFORMED: Expected {expected_cols} cols, got {len(row)}. Skipping.")
            continue
            
        processed_movie = {}
        invalid_rows = {}
        first_action_movie = None

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
                
            # Find and store the first movie where genres contains Action
            if not is_action_movie_found and col_name == 'genres' and 'Action' in cleaned_val:
                first_action_movie = processed_movie
                is_action_movie_found = True
            
            # Compute average rating_imdb and runtime_min as we go (optional, can be done in a second pass)
            # Accumulate sums and counts for averages.
            if col_name == 'rating_imdb' and processed_movie[col_name] is not None:
                if 'rating_sum' not in processed_movie:
                    processed_movie['rating_sum'] = 0.0
                    processed_movie['rating_count'] = 0
                processed_movie['rating_sum'] += processed_movie[col_name]
                processed_movie['rating_count'] += 1
            if col_name == 'runtime_min' and processed_movie[col_name] is not None:
                if 'runtime_sum' not in processed_movie:
                    processed_movie['runtime_sum'] = 0.0
                    processed_movie['runtime_count'] = 0
                processed_movie['runtime_sum'] += processed_movie[col_name]
                processed_movie['runtime_count'] += 1

            # Count how many movies have rating_imdb >= 8.0
            if col_name == 'rating_imdb' and processed_movie[col_name] is not None and processed_movie[col_name] >= 8.0:
                if 'high_rating_count' not in processed_movie:
                    processed_movie['high_rating_count'] = 0
                processed_movie['high_rating_count'] += 1

        # Step 3: Store the clean, validated row
        valid_movies.append(processed_movie)
        

# Compute and print final averages for rating_imdb and runtime_min
total_rating = sum(movie.get('rating_sum', 0) for movie in valid_movies)
count_rating = sum(movie.get('rating_count', 0) for movie in valid_movies)
average_rating = total_rating / count_rating if count_rating else "No valid ratings"   

total_runtime = sum(movie.get('runtime_sum', 0) for movie in valid_movies)
count_runtime = sum(movie.get('runtime_count', 0) for movie in valid_movies)
average_runtime = total_runtime / count_runtime if count_runtime else "No valid runtimes"  

print("\nAdditional Stats:")
print(f"\nFirst Action movie found at row {row_num}:\n\t{processed_movie}\n")

print("\nSummary of Averages:")
print(f"Average rating_imdb: {average_rating}")
print(f"Average runtime_min: {average_runtime}")

print("\nTotal movies with rating_imdb >= 8.0:", sum(movie.get('high_rating_count', 0) for movie in valid_movies))

# Optional: Print success message
print(f"\nProcessing complete. Successfully validated {len(valid_movies)} rows.")

print("\nRuntime complexities:" \
"\n" \
"For first action movie: O(n*m) where n is the number of rows and m is the number of columns. " \
"This is because we potentially check every cell in the dataset for validation. " \
"The average calculations are O(n) since we sum over all rows, " \
"but this is dominated by the initial O(n*m) validation step.    " \
"\n\n" \
"Space complexities:\n" \
"O(n) for storing the list of valid_movies, " \
"which grows linearly with the number of valid rows. " \
"Each movie is stored as a dictionary, but we are not storing the original raw data, " \
"so we are only keeping the cleaned and validated version in memory. " \
"The column blueprint and other auxiliary data structures are O(m), " \
"which is negligible compared to O(n) for large datasets." \
"If we had not stored the valid_movies and instead processed everything in a streaming fashion, " \
"the space complexity could be reduced to O(1) since we would only keep one row in memory at a time, " \
"but this would limit our ability to compute averages and other aggregate statistics " \
"without multiple passes through the data.")