import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def ask_gemini(prompt, model_name="gemini-2.5-flash"):

    # To test Gemini rate/limit handling, you can uncomment the following line to simulate a 429 error:
    # raise RuntimeError(
    #             "Test Gemini rate/limit reached. Please wait a minute and try again."
    #         )

    # Read your API key from the environment.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    # Build the remote Gemini endpoint URL.
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_name}:generateContent"
    )

    print(f"Sending request to Gemini model '{model_name}'...at this url:\n {url}\n")


    # Prepare the request body with your prompt.
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    # Create an HTTP POST request with JSON payload and API key.
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    # Send request, parse JSON response, and return only model text.
    # If quota/rate limit is reached, show a student-friendly message.
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as err:
        if err.code == 429:
            raise RuntimeError(
                "Gemini rate/limit reached. Please wait a minute and try again."
            ) from err
        raise

    return data["candidates"][0]["content"]["parts"][0]["text"].strip()

# Load file studio_ghibli_movies.csv into a dictionary using csv.DictReader 
# and find the missing data point. Print the row number and column where it is located.

import csv

with open("studio_ghibli_movies.csv", "r") as file:
    reader = csv.DictReader(file)
    
    count = 0
    ai_fix_count = 0
    ai_failed_fix_count = 0
    
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

                # Ask Gemini for the missing data point
                if column == "year":
                    prompt = f"What year was the Studio Ghibli movie '{row['title']}' released? \
                    Output format: only 4 digits, no extra text."
                elif column == "music_by":
                    prompt = f"Who composed the music for the Studio Ghibli movie '{row['title']}'? \
                    Output format: only the name, no extra text."

                try:
                    fixed_value = ask_gemini(prompt)
                    row[column] = fixed_value
                    ai_fix_count += 1
                    print(f"\nGemini's answer:\n {fixed_value}")
                    print(f"\nFixed data:\n {row}")
                except Exception as e:
                    print(f"Error occurred while asking Gemini: {e}")            
                    ai_failed_fix_count += 1
     
        cleaned_studio_ghibli_movies.append(row)
    
print(f"\nTotal missing data points filled by ai: {ai_fix_count}")
print(f"\nTotal missing data points that failed to be filled by ai: {ai_failed_fix_count}")

# Save the cleaned data to a new CSV file
with open("studio_ghibli_movies_cleaned.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = cleaned_studio_ghibli_movies[0].keys()  # Get fieldnames from the first row    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in cleaned_studio_ghibli_movies:
        writer.writerow(row)
print("Saved: studio_ghibli_movies_ai_clean.csv")



     


            