### Session 3 | Part 2

> Part 2 is quiz practice. These quizzes review complexity and the material from the lecture slides about hard-to-solve algorithms.

#### 1. Goal

You will practice:

- time and space complexity
- exponential and factorial growth
- divide and conquer
- greedy methods
- recursion and Fibonacci
- dynamic programming
- P, NP, NP-hard, and NP-complete

#### 2. Prerequisites

From the `session3` folder:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 3. Call Stelios to challenge you

Before starting the quizzes, call Stelios for one quick challenge question from the Session 3 challenge box.

#### 4. Multiple-choice quiz

This quiz checks the core vocabulary from the lecture: time complexity, space complexity, recursion, greedy methods, dynamic programming, and P/NP ideas.

```bash
quizmd --full-screen quizzes/python-complexity-and-algorithms-quiz.md
```

#### 5. Chaos quiz

The chaos quiz gives you a scenario and asks you to recover from bad design decisions. It focuses on choosing between streaming, generators, recursion, dynamic programming, and greedy shortcuts.

```bash
quizmd --full-screen quizzes/python-complexity-and-algorithms-chaos-quiz.md
```

#### 6. Session 2 chaos quiz

This chaos quiz reviews Session 2 material. It asks you to repair a messy CSV cleaning pipeline using `DictReader`, dictionary keys, missing-value checks, `strip()`, raw versus cleaned copies, and complexity.

```bash
quizmd --full-screen quizzes/python-session-02-data-cleaning-chaos-quiz.md
```

#### 7. Reverse quiz

The reverse quiz asks you to infer the concept from an output, a code snippet, or a short description. It is designed to test whether you can recognise an algorithmic idea when it appears in a different form.

```bash
quizmd --full-screen quizzes/python-complexity-and-algorithms-reverse-quiz.md
```

#### 8. Optional validation

If you want to check quiz file format:

```bash
quizmd --validate quizzes/python-complexity-and-algorithms-quiz.md
quizmd --validate quizzes/python-complexity-and-algorithms-chaos-quiz.md
quizmd --validate quizzes/python-session-02-data-cleaning-chaos-quiz.md
quizmd --validate quizzes/python-complexity-and-algorithms-reverse-quiz.md
```
