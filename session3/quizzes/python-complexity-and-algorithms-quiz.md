# Complexity and Hard Algorithms Quiz

## Question 1

A program checks every item in a list once.

If the list has `n` items, what is the time complexity?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 3
Type: single
Time: 45
Explanation: Checking each item once grows linearly with the number of items, so the time complexity is O(n).

## Question 2

A function stores only two counters while processing a very large file line by line.

What is the extra space complexity?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 1
Type: single
Time: 45
Explanation: The program keeps a fixed number of variables, so the extra space does not grow with input size.

## Question 3

An algorithm tries every possible subset of `n` items.

Which complexity best describes this kind of growth?

- O(log n)
- O(n log n)
- O(n²)
- O(2ⁿ)

Answer: 4
Type: single
Time: 50
Explanation: A set with `n` items has `2ⁿ` possible subsets, so this is exponential growth.

## Question 4

An algorithm tries every possible ordering of `n` cities for a route.

Which complexity best describes this?

- O(n)
- O(n!)
- O(n²)
- O(log n)

Answer: 2
Type: single
Time: 50
Explanation: Trying every ordering means checking all permutations, which grows factorially as O(n!).

## Question 5

Which idea best describes divide and conquer?

- Store previous answers to avoid repeated work
- Try every possible solution
- Always choose the locally best option
- Split the problem into smaller parts, solve them, then combine the results

Answer: 4
Type: single
Time: 50
Explanation: Divide and conquer breaks a problem into smaller subproblems and combines their solutions.

## Question 6

Which algorithmic strategy chooses the best-looking option at each step, hoping this leads to a good final answer?

- Dynamic programming
- Brute force
- Greedy method
- Recursion

Answer: 3
Type: single
Time: 45
Explanation: A greedy method makes the locally best choice at each step.

## Question 7

What must a recursive function have to avoid calling itself forever?

- A bigger input each time
- A base case
- A sorted list
- A second function

Answer: 2
Type: single
Time: 45
Explanation: A base case gives recursion a stopping point.

## Question 8

The naive recursive Fibonacci algorithm repeats many of the same calculations.

Which technique is commonly used to avoid this repeated work?

- Dynamic programming
- Random guessing
- Factorial search
- Loading all files into memory

Answer: 1
Type: single
Time: 50
Explanation: Dynamic programming stores or reuses answers to smaller subproblems, avoiding repeated Fibonacci calculations.

## Question 9

What does it mean for a problem to be in class P?

- A solution can be checked quickly, but not necessarily found quickly
- The problem has no possible algorithm
- The problem can be solved in polynomial time
- The problem must have factorial time complexity

Answer: 3
Type: single
Time: 50
Explanation: Problems in P can be solved in polynomial time.

## Question 10

What does NP-complete mean?

- The problem can only be solved with recursion
- The problem is always easy to solve
- The problem uses no memory
- The problem is in NP and is at least as hard as every problem in NP

Answer: 4
Type: single
Time: 55
Explanation: NP-complete problems are both in NP and NP-hard, meaning they are among the hardest problems in NP.
