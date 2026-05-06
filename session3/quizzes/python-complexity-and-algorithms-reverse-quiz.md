# Reverse Quiz: Complexity and Algorithms

## Question 1
Output:
0
1
1
2
3
5
8
13

Which sequence is this?

Options:
- Powers of 2
- Fibonacci numbers from F0 through F7
- Factorials from 0! through 7!
- Sorted job durations

Answer: 2
Type: single
Explanation: These are Fibonacci values from F0 to F7.

## Question 2
This code repeatedly calls itself with `n - 1` and `n - 2`.

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Which complexity best matches it?

Options:
- O(1)
- O(n)
- O(log n)
- O(2ⁿ)

Answer: 4
Type: single
Explanation: Naive recursive Fibonacci recomputes many values, causing exponential time.

## Question 3
A route planner tries every possible order of 9 cities.

Which growth pattern best describes this?

Options:
- O(1)
- O(n)
- O(n!)
- O(log n)

Answer: 3
Type: single
Explanation: Trying every permutation of cities is factorial growth.

## Question 4
A scheduling algorithm always places the next longest job on the currently least busy computer.

Which method does this sound like?

Options:
- Greedy
- Exhaustive search
- Dynamic programming
- Divide and conquer

Answer: 1
Type: single
Explanation: The algorithm makes a locally good choice at each step.

## Question 5
This method stores results so it does not solve the same subproblem again.

Which technique is being used?

Options:
- Random guessing
- Factorial brute force
- Dynamic programming
- Plain text parsing

Answer: 3
Type: single
Explanation: Dynamic programming stores and reuses subproblem results.

## Question 6
A problem is hard to solve, but a proposed solution can be checked quickly.

Which class idea does this describe?

Options:
- O(1)
- Greedy
- CSV
- NP

Answer: 4
Type: single
Explanation: NP problems have candidate solutions that can be verified quickly.

## Question 7
A problem is both in NP and NP-hard.

What is it called?

Options:
- P
- NP-complete
- Linear
- Divide-only

Answer: 2
Type: single
Explanation: NP-complete problems are both in NP and NP-hard.

## Question 8
An algorithm divides a problem into smaller subproblems, solves them, and combines the answers.

Which design approach is this?

Options:
- Greedy only
- Random walk
- Divide and conquer
- Factorial brute force

Answer: 3
Type: single
Explanation: Divide and conquer breaks a problem into smaller pieces and combines their solutions.
