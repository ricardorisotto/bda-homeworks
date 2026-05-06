### Session 3 | Part 1

> In Part 1, you will learn how Python can manage data in memory and process them one at a time. This matters when a file is too large to load into memory.

#### 1. Goal

You will:

- use iterables, iterators, `iter()`, and `next()`
- read a text file one line at a time
- write a simple generator with `yield`
- decide when to stream data and when to load all data
- describe the time and space complexity of each choice

#### 2. Prerequisites

Before starting:

1. In Visual Studio Code terminal, update your local repository.

```bash
git pull origin main
```

If this fails because you changed files and you only want to refresh the current `session3` folder, run:

```bash
git fetch origin
git restore --source origin/main --worktree --staged -- .
```

2. Open the `session3` folder in Visual Studio Code and in terminal.

```bash
cd session3
```

3. Create and activate your virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

4. Install requirements:

```bash
pip install -r requirements.txt
```

#### 3. Download the text dataset

Use the Birkbeck Hugging Face dataset:

- https://huggingface.co/datasets/Birkbeck/les-miserables-txt

Download:

```bash
hf download Birkbeck/les-miserables-txt les_miserables.txt --repo-type dataset --local-dir .
```

Expected file:

```txt
session3/les_miserables.txt
```

Run your scripts from the `session3` folder, so `open("les_miserables.txt", "r")` works directly.

For every exercise below:

1. Create or edit the file named in the instructions.
2. Copy the starter code into that file.
3. Complete the lines marked with comments such as `# Provide here your solution`.
4. Run the file from the `session3` folder.

Use this command whenever you update the exercise file:

```bash
python3 solutions/exercise-03-01.py
```

#### 4. Iterables and iterators

A list is an **iterable** because Python can loop over it using a `for` loop.

Create a small scratch file:

```txt
session3/solutions/exercise-03-00.py
```

Copy this code into the file and run it:

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

```bash
python3 solutions/exercise-03-00.py
```

An **iterator** remembers its current position, making it ideal when we want to move through a sequence index by index.

Replace the code in `session3/solutions/exercise-03-00.py` with this example and run it again:

```python
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

```bash
python3 solutions/exercise-03-00.py
```

After the last value, `next(it)` raises `StopIteration`. A `for` loop handles this automatically.

> [!TIP]
>
> What are the time and space complexities of reading one value with `next(it)`?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(1) for a list iterator.
>
> Space: O(1), because the iterator stores only its current position.
>
> </details>

#### 5. Files are iterators too

When you loop over a file, Python reads one line at a time. Create:

```txt
session3/solutions/exercise-03-01.py
```

Copy this code into `session3/solutions/exercise-03-01.py`:

```python
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    it = iter(file)
    print(next(it))
    print(next(it))
```

> [!TIP]
>
> What are the time and space complexities?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(m) per line, where `m` is the length of the line being read.
>
> Space: O(m), because only one line is held at a time.
>
> </details>

#### 6. Exercise: print the first record

Task:

1. Open `les_miserables.txt`.
2. Print only the first line.
3. Do not use `readlines()`.

Copy this skeleton into `session3/solutions/exercise-03-01.py`:

```python
TEXT_FILE = "les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    # Provide here your solution
    ...
```

> [!TIP]
>
> Should this use streaming or loading all data?
>
> <details>
> <summary>Show answer</summary>
>
> Streaming. You only need the first record.
>
> ```python
> TEXT_FILE = "les_miserables.txt"
>
> with open(TEXT_FILE, "r", encoding="utf-8") as file:
>     first = next(file)
>     print(first)
> ```
>
> Time: O(m), where `m` is the length of the first line.
>
> Space: O(m).
>
> If the file is empty, `next(file)` will raise `StopIteration`. For a safer version:
>
> ```python
> TEXT_FILE = "les_miserables.txt"
>
> with open(TEXT_FILE, "r", encoding="utf-8") as file:
>     first = next(file, "")
>     print(first)
> ```
>
> </details>

#### 7. Exercise: find the first line containing text

Find the first line containing `target = "Jean Valjean"`.

Replace the code in `session3/solutions/exercise-03-01.py` with this skeleton:

```python
TEXT_FILE = "les_miserables.txt"
target = "Jean Valjean"
found = None

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        ...

print(found)
```

> [!TIP]
>
> Why is `break` useful here?
>
> <details>
> <summary>Show answer</summary>
>
> It stops once the first match is found. We do not need to read the rest of the file.
>
> ```python
> TEXT_FILE = "les_miserables.txt"
> target = "Jean Valjean"
> found = None
>
> with open(TEXT_FILE, "r", encoding="utf-8") as file:
>     for line in file:
>         if target in line:
>             found = line
>             break
>
> print(found)
> ```
>
> Best case time: O(m), if the match is near the start.
>
> Worst case time: O(n * m), if Python must check all `n` lines.
>
> Space: O(m), because only one line is processed at a time.
>
> </details>

#### 8. Exercise: count all lines

Count how many lines are in the file.

Replace the code in `session3/solutions/exercise-03-01.py` with this skeleton:

```python
TEXT_FILE = "les_miserables.txt"
count = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        ...

print(count)
```

> [!TIP]
>
> Do we need all lines in memory?
>
> <details>
> <summary>Show answer</summary>
>
> No. A counter is enough.
>
> ```python
> TEXT_FILE = "les_miserables.txt"
> count = 0
>
> with open(TEXT_FILE, "r", encoding="utf-8") as file:
>     for line in file:
>         count += 1
>
> print(count)
> ```
>
> Time: O(n), where `n` is number of lines.
>
> Space: O(1) extra space, ignoring the current line buffer.
>
> </details>

#### 9. Exercise: average line length

Compute the average line length.

Replace the code in `session3/solutions/exercise-03-01.py` with this skeleton:

```python
TEXT_FILE = "les_miserables.txt"
total_length = 0
count = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        # Provide here your solution
        ...

average = total_length / count
print(average)
```

> [!TIP]
>
> Do we need to store all lines?
>
> <details>
> <summary>Show answer</summary>
>
> No. We only need a running total and a counter.
>
> ```python
> TEXT_FILE = "les_miserables.txt"
> total_length = 0
> count = 0
>
> with open(TEXT_FILE, "r", encoding="utf-8") as file:
>     for line in file:
>         total_length += len(line)
>         count += 1
>
> average = total_length / count
> print(average)
> ```
>
> Time: O(n), if we treat `len(line)` as constant per line for this discussion.
>
> More precisely: O(total characters).
>
> Space: O(1) extra space.
>
> </details>

#### 10. When do we need to load all data?

Sometimes streaming is not enough.

Use loading all data when you need:

- indexing, such as `lines[100]`
- sorting all lines
- repeated passes over the same data
- comparing each line with many other lines
- sending a selected batch of lines to another function

Example:

Replace the code in `session3/solutions/exercise-03-01.py` with this example:

```python
TEXT_FILE = "les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines[100])
```

> [!TIP]
>
> What is the complexity when loading all lines?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n), or more precisely O(total characters).
>
> Space: O(n * m), because all lines are stored.
>
> </details>

#### 11. Generators with `yield`

A generator is a function that produces values one at a time.

Replace the code in `session3/solutions/exercise-03-01.py` with this example:

```python
def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line
```

Add this code below the `non_empty_lines()` function in the same file:

```python
for line in non_empty_lines("les_miserables.txt"):
    print(line)
    break
```

`yield` is different from `return`:

- `return` gives back one final value and stops the function.
- `yield` gives back one value, pauses, and continues later.

> [!TIP]
>
> A generator is useful when the dataset is large and you only need one item at a time.



#### 12. Exercise: Count non-empty lines containing a word

Write a program that counts how many non-empty lines contain the word `"Jean"` using `yield`.

Replace the code in `session3/solutions/exercise-03-01.py` with this skeleton:

```python
TEXT_FILE = "les_miserables.txt"
target = "Jean"

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # Complete the generator:
            # 1. Remove spaces and newline characters
            # 2. Yield only non-empty lines
            ...

count = 0

# Use non_empty_lines(TEXT_FILE) to count
# how many non-empty lines contain target

print(count)
```

> [!TIP]
>
> What are the time and space complexities?
>
> <details>
> <summary>Show answer</summary>
>
> ```python
> TEXT_FILE = "les_miserables.txt"
> target = "Jean"
>
> def non_empty_lines(path):
>     with open(path, "r", encoding="utf-8") as file:
>         for line in file:
>             line = line.strip()
>             if line != "":
>                 yield line
>
> count = 0
>
> for line in non_empty_lines(TEXT_FILE):
>     if target in line:
>         count += 1
>
> print(count)
> ```
>
> Time: O(n * m), where `n` is the number of lines and `m` is the average line length.
>
> Space: O(m), because one stripped line is processed at a time.
>
> </details>

#### 13. Practice: streaming or loading

The next practice step is to run two quizzes about choosing the correct code when the strategy is `streaming` or `load all`.

First, run the multiple-choice quiz:

```bash
quizmd --full-screen quizzes/python-streaming-vs-loading-code-quiz.md
```

Then, run the reverse quiz:

```bash
quizmd --full-screen quizzes/python-streaming-vs-loading-reverse-quiz.md
```
