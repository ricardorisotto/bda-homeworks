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


