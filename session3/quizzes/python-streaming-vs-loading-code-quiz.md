# Streaming or Load All: Choose the Code

## Question 1

Strategy: `load all`

Task: Print line number 10,000 five times.

Which code best matches the strategy?

```python
# A
for i in range(5):
    with open("les_miserables.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number == 10000:
                print(line)
                break
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i in range(5):
    print(lines[9999])
```

- A
- B
- Both
- Neither

Answer: 2
Type: single
Time: 50
Explanation: B loads the file once and then uses direct indexing. A repeatedly scans from the start of the file.

## Question 2

Strategy: `streaming`

Task: Print the first 20 non-empty lines without reading the rest of the file.

Which code best matches the strategy?

```python
# A
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

non_empty = [line.strip() for line in lines if line.strip() != ""]
for line in non_empty[:20]:
    print(line)
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    text = file.read()

non_empty = [line.strip() for line in text.splitlines() if line.strip() != ""]
for line in non_empty[:20]:
    print(line)
```

- A
- B
- Both
- Neither

Answer: 4
Type: single
Time: 55
Explanation: Neither version is a good streaming solution. A loads all lines, and B loads the whole file as one string.

## Question 3

Strategy: `streaming`

Task: Print only the first line of `les_miserables.txt`.

Which code best matches the strategy?

```python
# A
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    first = next(file)
    print(first)
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines[0])
```

- A
- B
- Both
- Neither

Answer: 1
Type: single
Time: 45
Explanation: A reads just the first line. B loads the whole file before printing line 1.

## Question 4

Strategy: `streaming`

Task: Find the first line containing `Fantine`.

Which code best matches the strategy?

```python
# A
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

matches = [line for line in lines if "Fantine" in line]
print(matches[0])
```

```python
# B
found = None
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "Fantine" in line:
            found = line
            break

print(found)
```

- A
- B
- Both
- Neither

Answer: 2
Type: single
Time: 50
Explanation: B streams line by line and stops as soon as it finds the first match. A loads every line first.

## Question 5

Strategy: `streaming`

Task: Count all lines without storing them.

Which code best matches the strategy?

```python
# A
count = 0
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print(count)
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    count = sum(1 for line in file)

print(count)
```

- A
- B
- Both
- Neither

Answer: 3
Type: single
Time: 45
Explanation: Both versions read the file line by line and keep only a count.

## Question 6

Strategy: `streaming`

Task: Count how many lines contain `Valjean` without storing the matching lines.

Which code best matches the strategy?

```python
# A
count = 0
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "Valjean" in line:
            count += 1

print(count)
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

matches = [line for line in lines if "Valjean" in line]
print(len(matches))
```

- A
- B
- Both
- Neither

Answer: 1
Type: single
Time: 50
Explanation: A streams through the file and keeps only a counter. B stores all lines and then stores the matching lines.

## Question 7

Strategy: `load all`

Task: Compare the first 100 lines against each other to find duplicate lines.

Which code best matches the strategy?

```python
# A
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
        break
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()[:100]

duplicates = []
for i, left in enumerate(lines):
    for right in lines[i + 1:]:
        if left == right:
            duplicates.append(left)

print(duplicates)
```

- A
- B
- Both
- Neither

Answer: 2
Type: single
Time: 55
Explanation: B keeps the first 100 lines together so they can be compared with each other. A only prints the first line.

## Question 8

Strategy: `load all`

Task: Sort every line alphabetically.

Which code best matches the strategy?

```python
# A
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines.sort()
print(lines[:10])
```

```python
# B
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

- A
- B
- Both
- Neither

Answer: 1
Type: single
Time: 45
Explanation: A loads all lines so they can be sorted together. B streams through the file and does not sort.
