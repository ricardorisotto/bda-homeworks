# Chaos: Algorithm Choices Under Pressure
Type: chaos
Title: Fixing a slow text-analysis script
Skills: complexity, streaming, generators, yield, recursion, dynamic-programming
Difficulty: medium

## Scenario
You are helping a team analyse `les_miserables.txt`.
The file may become very large, and the first version of the script is too slow and uses too much memory.

The team needs to:

1. build a short excerpt using only useful non-empty lines,
2. count lines containing a target word,
3. avoid unnecessary repeated work,
4. explain the time and space complexity.

## Decision 1
What is your first design choice?

- A. Use `readlines()` everywhere so every function can access the whole file
- B. Use naive recursion for repeated calculations because recursion is always efficient
- C. Use a greedy shortcut for every task because it is usually fast
- D. Stream the file and create a generator with `yield` for non-empty lines

Answer: D
Score: 3

### Feedback
The strongest first design is to stream the file. A generator lets the program produce one useful line at a time.

### Chaos if A
Memory usage jumps when the dataset grows. Loading all lines is convenient, but it creates O(n) extra space when the task only needs one line at a time.

### Chaos if B
The script repeats the same subproblems many times. Naive recursion can become exponential when overlapping subproblems are not stored or reused.

### Chaos if C
The shortcut gives a fast answer, but it is not always the correct answer. Greedy choices need a reason why the local best step leads to a good final result.

### Chaos if D
Good start, but two separate chaos events hit your generator:

1. It accidentally uses `return line` instead of `yield line`, so it stops after one line.
2. Oh no, there are empty and whitespace-only lines. The excerpt should not include blank lines.

## Path A
### Recovery A
The script currently does this:

```text
1  with open("les_miserables.txt", "r", encoding="utf-8") as file:
2      lines = file.readlines()
3
4  count = 0
5  for line in lines:
6      if "Jean" in line:
7          count += 1
```

What is the best recovery?

- A. Keep `readlines()` because O(n) space is always fine
- B. Loop over the file directly and keep only a counter
- C. Sort all lines before counting
- D. Try every possible subset of lines

Answer: B
Score: 2

### Feedback
Recovered. Counting matches can be done by streaming through the file once and keeping O(1) extra space.

## Path B
### Recovery B
The team wrote a naive recursive function that repeats the same calculations again and again.

Which idea should you introduce?

- A. Dynamic programming
- B. Factorial search
- C. Loading all text files into memory
- D. Random guessing

Answer: A
Score: 2

### Feedback
Recovered. Dynamic programming stores or reuses answers to overlapping subproblems, such as repeated Fibonacci calls.

## Path C
### Recovery C
The team wants to use a greedy method for every hard problem.

What should you tell them?

- A. Greedy methods are always optimal
- B. Greedy methods are never useful
- C. Greedy methods need evidence that local choices produce a good final answer
- D. Greedy methods are the same as dynamic programming

Answer: C
Score: 2

### Feedback
Recovered. Greedy methods can be useful, but they need a correctness argument or a clear reason why the shortcut is acceptable.

## Path D
### Recovery D
The generator currently looks like this:

```text
1  def non_empty_lines(path):
2      with open(path, "r", encoding="utf-8") as file:
3          for line in file:
4              return line
```

How should it handle both chaos events?

- A. Keep `return line` and remove empty lines later
- B. Add `readlines()` before the loop
- C. Strip each line, skip empty strings, and `yield line`
- D. Sort the file before yielding

Answer: C
Score: 3

### Feedback
Correct. The generator should clean each line, skip empty strings, and use `yield` to produce useful lines one at a time.

## Final Decision
You have repaired the first design. What final explanation should you give?

- A. The best algorithm is always the one with the shortest code
- B. Exponential and factorial algorithms are fine for any input size
- C. NP-complete problems can always be solved quickly with a greedy method
- D. The generator version streams useful lines one at a time, uses O(1) extra space, and avoids loading the whole file

Answer: D
Score: 4

### Final feedback
Strong final decision. The explanation connects the code choice to time and space complexity, and it correctly separates streaming from harder algorithmic problems.

## Result
Maximum score: 10

- 9-10: Excellent. You chose a scalable design and recovered well from the chaos.
- 6-8: Good. You understand the main ideas, with a few recovery points to review.
- 3-5: Partial understanding. Review streaming, generators, and repeated subproblems.
- 0-2: Needs practice. Revisit complexity, `yield`, recursion, and greedy methods.
