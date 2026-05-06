# Streaming and Generators Theory Quiz

## Question 1

In Python, what is an iterable?

- A file that has already been fully loaded into memory
- An object that Python can loop over
- A function that must use `return`
- A variable that stores only numbers

Answer: 2
Type: single
Time: 45
Explanation: An iterable is something Python can loop over, such as a list, string, file, or generator.

## Question 2

What does an iterator remember?

- Its current position in a sequence
- Every possible future value
- The total memory used by Python
- The name of the source file only

Answer: 1
Type: single
Time: 45
Explanation: An iterator remembers where it is, so repeated calls to `next()` move forward through the values.

## Question 3

Which statements about file iteration are correct? Select two.

- A file loop always stores all lines in a list first
- Looping over a file reads one line at a time
- `readlines()` is required before every file loop
- A file object can be used with `iter()` and `next()`

Answer: 2,4
Type: multiple
Time: 60
Explanation: Files can be streamed line by line, and file objects are iterable. `readlines()` loads all lines and is not required for looping.

## Question 4

For the task "print only the first line of a large file", which strategy is usually best?

- Load all lines with `readlines()`
- Sort the file first
- Compare every line with every other line
- Stream the file and read one line

Answer: 4
Type: single
Time: 45
Explanation: Only the first line is needed, so streaming avoids unnecessary memory use.

## Question 5

Which tasks usually require loading all selected data into memory? Select two.

- Sort every line alphabetically
- Access line 10,000 many times
- Print only the first line
- Count all lines

Answer: 1,2
Type: multiple
Time: 60
Explanation: Sorting needs the lines together, and repeated random access is easier after loading. First-line printing and counting can stream.

## Question 6

What does `yield` do in a generator function?

- It stops the program immediately
- It creates a list containing all results
- It gives one value, pauses the function, and can continue later
- It imports data from Hugging Face

Answer: 3
Type: single
Time: 50
Explanation: `yield` produces one value at a time and keeps the function state for the next request.

## Question 7

Which statements about `yield` and `return` are correct? Select two.

- `yield` always makes the time complexity O(1)
- `return` gives back one final value and stops the function
- `return` automatically streams a file line by line
- `yield` can produce a sequence of values over time

Answer: 2,4
Type: multiple
Time: 60
Explanation: `return` ends the function, while `yield` lets a generator produce values one at a time. `yield` does not magically make all work constant time.

## Question 8

You count all lines in a file by looping over the file and keeping only a counter.

What is the extra space complexity?

- O(n), because all lines must be stored
- O(log n), because the file is searched
- O(1), ignoring the current line buffer
- O(n²), because the file has many lines

Answer: 3
Type: single
Time: 50
Explanation: The program keeps a fixed number of variables, so the extra space is constant apart from the current line being read.

## Question 9

You search for the first line containing `"Jean Valjean"` and stop with `break` when it is found.

Which statements are correct? Select two.

- `break` forces Python to read the rest of the file
- The best case can be fast if the match is near the start
- The worst case may still check every line
- This task always needs `readlines()`

Answer: 2,3
Type: multiple
Time: 60
Explanation: `break` lets the search stop early, but if the match is late or missing, the loop may inspect the whole file.

## Question 10

A generator yields non-empty lines from a very large text file. Another loop counts how many yielded lines contain `"Jean"`.

Which complexity description is most accurate?

- Time is always O(1), because generators use `yield`
- Space is always O(n), because generators store every yielded value
- The program must load all lines before it can count
- Time can be O(total characters checked), and extra space can stay small

Answer: 4
Type: single
Time: 70
Explanation: The program may still inspect many characters, but it can avoid storing the whole file by processing one yielded line at a time.
