# Essay Question: Complexity Basics

## Question
Describe the time complexity of:
A) searching a number in an unsorted list
B) searching a number in a sorted list using binary search
C) sorting a list using bubble sort

## Instructions for Students
Answer in 5-8 lines. Use Big-O notation.

## Instructor Name
Stelios

## Hint
Think about how many elements may need to be checked as `n` grows.

## Evaluation Criteria (Total: 6 points)
1. **A: Linear search (2 points)**
- Correctly states `O(n)`.

2. **B: Binary search (2 points)**
- Correctly states `O(log n)`.
- Mentions that binary search requires a sorted list.

3. **C: Bubble sort (2 points)**
- Correctly states average/worst `O(n^2)`.
- Optional bonus detail: best case `O(n)` with optimization (early-stop flag).

## Reference Answer
A) `O(n)` for searching in an unsorted list.
B) `O(log n)` for binary search on sorted data.
C) Bubble sort is `O(n^2)` on average and worst case.

## AI Evaluation Rules
Grade only by criteria above. Do not use external assumptions.
Accept equivalent wording when the underlying complexity idea is correct.
If a student gives correct complexity but misses the sorted-list condition for binary search, deduct only from criterion B.

## Output Format
Return JSON with points, did_well, missing, suggestions.
