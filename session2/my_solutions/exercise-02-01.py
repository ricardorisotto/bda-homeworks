import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["genres"])

import csv

count = 0

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["year"] == "2020":
            count += 1

print("Number of movies released in 2020:", count)

import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Action" in row["genres"]:
            print("First movie with 'Action' genre:", row)
            break

import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Field names:")
    print(reader.fieldnames)

    print("\nFirst 5 data rows:")
    for i, row in enumerate(reader):
        if i < 5:
            print(row)
        else:
            break

    # Count movies from USA
    file.seek(0)  # Reset file pointer to the beginning
    reader = csv.DictReader(file)  # Recreate reader to read from the beginning
    count = 0
    for row in reader:
        if row["country"] == "USA":
            count += 1
    print("Number of movies from USA:", count)

    # Find first movie where genres is exactly Action
    file.seek(0) # Reset file pointer to the beginning
    reader = csv.DictReader(file) # Recreate reader to read from the beginning
    for row in reader:
        if row["genres"] == "Action":
            print("First movie where genres is exactly Action:", row)
            break

     # Find first movie where Action appears inside genres
    file.seek(0) # Reset file pointer to the beginning
    reader = csv.DictReader(file) # Recreate reader to read from the beginning
    for row in reader:
        if "Action" in row["genres"]:
            print("First movie where Action appears inside genres:", row)
            break
    
    # One benefit of csv.DictReader instead of csv.reader is that we can use column names, 
    # which is clearer than numeric indexes.
    
    print("\nComplexity:")
    print("Field names: time O(1), space O(1)")
    print("First 5 rows: time O(1), space O(1)")
    print("USA count: time O(n), space O(1)")
    print("First-match searches: time O(n), space O(1)")

import csv

with open("data/movies_incomplete/movies.csv", "r") as file:
    reader = csv.DictReader(file)
    
    count = 0
    # Find the missing data point and print row and column
    for row in reader:
        for column, value in row.items():
            if not value:
                print(f"\nMissing data in row number {reader.line_num}  : {row}, \ncolumn: {column}")
                count += 1

print(f"\nTotal missing data points: {count}")

with open("data/movies_incomplete/movies.csv", "r") as file:
    reader = csv.DictReader(file)
    
    # Find the average of votes column, ignoring missing values
    total_votes = 0
    count = 0
    for row in reader:
        if row["votes"]:
            total_votes += int(row["votes"])
            count += 1 

if count > 0:
    average_votes = total_votes / count
    print(f"\nAverage votes: {average_votes}")
else:
    print(f"\nNo valid vote data available.")       