# Chaos: Movie CSV Cleaning Under Pressure
Type: chaos
Title: Repairing a messy CSV cleaning pipeline
Skills: csv, DictReader, dictionaries, missing-values, strip, copying, complexity
Difficulty: medium

## Scenario
You are helping a team clean a movie dataset from Session 2.
The first version of the script mixes up list indexes, dictionary keys, missing values, and cleaned output.

The team needs to:

1. read CSV rows using column names,
2. find missing values safely,
3. fix selected missing values,
4. keep a raw copy and a cleaned copy,
5. save the cleaned rows,
6. explain the time and space complexity.

## Decision 1
What is your first design choice?

- A. Treat empty strings as valid data and skip cleaning
- B. Use numeric indexes like `row[3]` because they are always clearer
- C. Use `csv.DictReader` so each row can be accessed by column name
- D. Edit the original data directly and keep no raw copy

Answer: C
Score: 3

### Feedback
The strongest first design is to use `csv.DictReader`. Column names such as `row["year"]` and `row["music_by"]` make the cleaning code easier to read and less fragile.

### Chaos if A
The missing values stay hidden. A cell containing `"   "` looks non-empty unless the script strips whitespace.

### Chaos if B
The script breaks when the CSV column order changes. Numeric indexes are fragile because `row[3]` does not explain which field is being used.

### Chaos if C
Good start, but three problems appear:

1. Some missing values contain spaces, so `value == ""` misses them.
2. Numeric fields such as `year` are still strings.
3. The team wants a raw copy and a cleaned copy.

### Chaos if D
The team cannot compare raw data with cleaned data later. Editing the only copy removes useful evidence about what changed.

## Path A
### Recovery A
The missing-value check currently looks like this:

```text
1  for row in rows:
2      if row["music_by"] == "":
3          print("missing music")
```

What is the best recovery?

- A. Sort the rows before checking them
- B. Use `row["music_by"] == "missing"`
- C. Delete every row with a blank field
- D. Use `row["music_by"].strip() == ""`

Answer: D
Score: 2

### Feedback
Recovered. `strip()` removes spaces and newline characters, so whitespace-only values are detected as missing.

## Path B
### Recovery B
The script currently reads rows with numeric indexes.

```text
1  reader = csv.reader(file)
2  for row in reader:
3      print(row[3])
```

What should you change?

- A. Keep numeric indexes because headers do not matter
- B. Use `csv.DictReader(file)` and access values with keys such as `row["genres"]`
- C. Delete the header row and guess the column order
- D. Convert every row into one long string

Answer: B
Score: 2

### Feedback
Recovered. `DictReader` uses header names as dictionary keys, which makes the script clearer and safer when columns are named.

## Path C
### Recovery C
The team says: "We can ignore missing values. The average year will still work."

What should you tell them?

- A. Empty strings always convert to integer zero
- B. `strip()` automatically calculates averages
- C. Missing years should be detected and fixed or skipped before numeric calculations
- D. CSV files cannot contain missing values

Answer: C
Score: 2

### Feedback
Recovered. Numeric calculations need clean numeric values. Empty strings or whitespace-only fields should be handled before conversion.

## Path D
### Recovery D
The team edited the original list directly and now wants to compare raw data with cleaned data.

What should they do next time?

- A. Make separate copies, such as `original_movies` and `cleaned_movies`, before editing
- B. Use `readlines()` instead of dictionaries
- C. Keep only the cleaned data because raw data is never useful
- D. Save the data before checking missing values

Answer: A
Score: 2

### Feedback
Recovered. Keeping a raw copy and a cleaned working copy makes the cleaning process easier to inspect and explain.

## Final Decision
You have repaired the cleaning pipeline. What final explanation should you give?

- A. The best cleaning script always mutates the original rows and skips validation
- B. Complexity does not matter once the data is saved
- C. A CSV cleaning script should avoid dictionaries because keys are slower to type
- D. The cleaned pipeline reads named columns, strips values before checking for blanks, fixes selected fields, preserves a raw copy, and saves cleaned output

Answer: D
Score: 4

### Final feedback
Strong final decision. The explanation connects Session 2 ideas: dictionary rows, `strip()`, missing-value repair, raw versus cleaned data, output files, and complexity.

## Result
Maximum score: 9

- 8-9: Excellent. You repaired the cleaning pipeline and explained the trade-offs clearly.
- 6-8: Good. You understand most of the CSV and cleaning workflow.
- 3-5: Partial understanding. Review `DictReader`, missing values, and raw versus cleaned copies.
- 0-2: Needs practice. Revisit Session 2 dictionary rows and cleaning steps.
