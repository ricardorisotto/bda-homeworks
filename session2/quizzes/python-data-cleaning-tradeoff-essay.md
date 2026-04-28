# Essay Question: choose the better cleaning approach

## Question
Assume that `my_data` is a list with many rows, and some values are missing (represented as empty strings "").

You can:
1. Clean in place (modify the original list directly), or
2. Copy first to a new list, then clean the copied list.

Compare the two approaches in terms of:
- time complexity
- space complexity
- risk/safety

Then explain which option you would choose for:
- a quick one-off local script
- a production workflow where raw data must be preserved

Be specific with Big-O notation (for example `O(n)`, `O(1)`, `O(n)` extra space).

## Instructions for Students
Write 10-14 lines.

## Instructor Name
Stelios

## Hint
🤔 Hint: In real-world systems, it’s important to be able to undo changes and trace what happened, not just run things quickly.

## Evaluation Criteria (Total: 4 points)
1. **Complexity comparison accuracy (1 point)**
- Correctly states:
  - in-place clean: `O(n)` time, `O(1)` extra space
  - copy-first clean: `O(n)` copy + `O(n)` clean (overall linear), `O(n)` extra space
- We expect both options to be discussed, not just one.
- We expect a short justification of *why* the space differs (copy allocation vs no copy).
2. **Risk/safety reasoning (1 point)**
- Explains mutation risk and why preserving raw data matters
- We expect mention of at least one concrete risk (for example accidental overwrite, difficult rollback, harder auditing).
- We expect explanation of why preserving raw data improves verification and debugging.
3. **Context-aware choice (1 point)**
- Gives different reasonable choices for one-off vs production contexts
- We expect one clear recommendation for a quick local script and one for production.
- We expect the recommendation to be tied to constraints (memory budget, reliability, auditability, recovery needs).
4. **Clarity and structure (1 point)**
- Response is organized, specific, and practical
- We expect clear wording with minimal ambiguity and consistent use of terms like in-place, copy-first, and extra space.
- We expect the answer to stay within the requested length while still addressing all required bullets.

## Reference Answer
Let `n` be the number of rows in `my_data`.

In-place cleaning scans rows and updates missing values directly, so time is `O(n)`. It does not allocate another full dataset, so extra space is `O(1)` (excluding loop variables and small helpers).

Copy-first cleaning first duplicates the dataset (`O(n)` time and `O(n)` extra space), then scans/updates the copy (`O(n)` time). Total time is still linear (`O(n) + O(n) = O(n)`), but memory overhead is larger because both raw and working data coexist.

Tradeoff:
- In-place: better memory efficiency and usually simpler for quick one-off scripts, but higher mutation risk if cleaning rules are wrong.
- Copy-first: safer for production because it preserves raw data for validation, rollback, auditing, and reproducibility, at the cost of extra memory.

Practical choice:
- Quick local script with limited risk: often in-place.
- Production or high-stakes workflow: usually copy-first.

## AI Evaluation Rules
Evaluate only by the rubric above.
Do not use external knowledge.
Score = (points achieved / 4) x 100.
Accept equivalent phrasing and related concepts, not only exact wording from the reference answer.
Award credit when the student uses correct ideas with different terminology (for example "duplicate list", "backup copy", "preserve source of truth", "restore/revert path", "traceability/audit trail").
Do not penalize minor notation differences if complexity reasoning is correct (for example `O(n)+O(n)` vs "still linear").
When partially correct, give partial credit in the relevant criterion and explain exactly what is missing.

## Output Format
Score: XX%

Feedback:
- What the student did well
- What is missing
- 1-2 suggestions for improvement
