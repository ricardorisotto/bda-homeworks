movies = [
    {
        "title": "Howl's Moving Castle",
        "year": "2004",
        "director": "Hayao Miyazaki",
        "music_by": "",
    },
    {
        "title": "Kiki's Delivery Service",
        "year": "",
        "director": "Hayao Miyazaki",
        "music_by": "Joe Hisaishi",
    },
]

for i, movie in enumerate(movies, start=1):
    for key, value in movie.items():
        if value.strip() == "":
            print(f"Record {i} missing field: {key}")

for i, movie in enumerate(movies, start=1):
    if movie["music_by"].strip() == "":
        print(f"Record {i} missing field: music_by")
    if movie["year"].strip() == "":
        print(f"Record {i} missing field: year")

if movies[0]["music_by"].strip() == "":
    movies[0]["music_by"] = "Joe Hisaishi"

if movies[1]["year"].strip() == "":
    movies[1]["year"] = "1989"

print(movies)

original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy() for movie in movies]

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"

print("\nOriginal:\n", original_movies)
print("\nCleaned:\n", cleaned_movies)

import json

with open("movies_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

print("Saved: movies_clean.json")

# Load file studio_ghibli_movies.csv into a dictionary using csv.DictReader 
# and find the missing data point. Print the row number and column where it is located.

import csv

with open("studio_ghibli_movies.csv", "r") as file:
    reader = csv.DictReader(file)
    
    count = 0
    
    # Calculating average year of movies
    total_years = 0
    count_years = 0

    # Count number of times Miyazaki appears as director
    miyazaki_count = 0

    # Cleaned studio_ghibli_movies.csv by filling in missing data points
    cleaned_studio_ghibli_movies = []
    
    # Find the missing data point and print row and column
    for row in reader:
        for column, value in row.items():
            if not value.strip():
                print(f"\nMissing data in row number {reader.line_num} :\n {row}, \ncolumn: {column}")

                # Fix the missing data point
                if column == "music_by" and row["title"] == "Howl's Moving Castle":
                    row[column] = "Joe Hisaishi"
                elif column == "year" and row["title"] == "Kiki's Delivery Service":
                    row[column] = "1986"
                elif column == "year" and row["title"] == "Ponyo":
                    row[column] = "1988"

                print(f"\nFixed data:\n {row}")

                count += 1
                if row["year"].strip():
                    total_years += int(row["year"])
                    count_years += 1
                
                if row["director"] == "Hayao Miyazaki":
                    miyazaki_count += 1
                
        cleaned_studio_ghibli_movies.append(row)
    
    print(f"\nAverage year: {total_years / count_years if count_years > 0 else 0}")
    print(f"\nMiyazaki count: {miyazaki_count}")

# Save the cleaned data to a new CSV file
with open("studio_ghibli_movies_cleaned.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = cleaned_studio_ghibli_movies[0].keys()  # Get fieldnames from the first row    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in cleaned_studio_ghibli_movies:
        writer.writerow(row)
print("Saved: studio_ghibli_movies_cleaned.csv")

# Time complexity of the above code is O(n*m) where n is the number of rows and m is the number of columns,
#  because we are iterating through each row and then through each column to check for missing values. 
# But since the number of columns is much smaller than the number of rows, 
# we can consider it O(n) in practice.
# 
# Space complexity is O(n) for storing the cleaned data.

            