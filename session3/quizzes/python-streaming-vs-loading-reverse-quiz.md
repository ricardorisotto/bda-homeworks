# Reverse Quiz: Streaming vs Loading

## Question 1

Read the code.

```python
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))
print(next(it))
```

Which output does this code produce?

Options:
- 1 then 1
- 1 then 2
- 2 then 3
- StopIteration immediately

Answer: 2
Type: single
Time: 45
Explanation: The iterator remembers its position, so the first `next(it)` gives `1` and the second gives `2`.

## Question 2

Read the code.

```python
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines[100])
```

Which description best matches this code?

Options:
- It reads only one line from disk
- It is the best choice when the file is too large for memory
- It streams the file one character at a time
- It loads all lines before using an index

Answer: 4
Type: single
Time: 45
Explanation: `readlines()` stores all lines in a list, which then allows indexing with `lines[100]`.

## Question 3

Read the code.

```python
found = None

with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "Jean Valjean" in line:
            found = line
            break

print(found)
```

What is the main benefit of `break` here?

Options:
- It stops reading after the first match is found
- It loads all matching lines into memory
- It sorts the file before searching
- It prevents the file from opening

Answer: 1
Type: single
Time: 45
Explanation: Once the first matching line is found, `break` stops the loop so the rest of the file does not need to be read.

## Question 4

Read both snippets.

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
total_length = 0
count = 0
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        total_length += len(line)
        count += 1
print(total_length / count)
```

Which statement is correct?

Options:
- A streams, but B must load all lines
- B streams, but A must load all lines
- Both process one line at a time without storing the whole file
- Neither uses a file iterator

Answer: 3
Type: single
Time: 50
Explanation: Both snippets loop over the file directly and keep only small variables such as counters and totals.

## Question 5

Read the code.

```python
def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

for line in non_empty_lines("les_miserables.txt"):
    print(line)
    break
```

Which description best matches this code?

Options:
- `yield` returns the whole file as one final value
- The generator produces non-empty lines one at a time
- `break` makes the generator load all remaining lines
- `strip()` sorts the lines alphabetically

Answer: 2
Type: single
Time: 50
Explanation: The generator uses `yield` to produce one non-empty line at a time, and the loop stops after printing the first one.
