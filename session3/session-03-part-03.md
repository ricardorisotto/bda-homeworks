### Session 3 | Part 3

> In Part 3, you will run the most basic version of RAG over *Les Misérables*.

#### 1. Goal

RAG means **retrieval-augmented generation**.

The whole idea is:

```txt
find useful text first -> send that text to Gemini -> get an answer
```

An LLM does not automatically know what is inside your local text file. RAG is one way to give it useful text at the moment you ask a question.

In this tutorial, we will:

1. read *Les Misérables* line by line,
2. retrieve a few lines that look relevant,
3. place those lines inside the prompt,
4. ask Gemini to answer using that context.

This is not a full search engine. It is the smallest useful version of the idea.

#### 2. Prerequisites

Part 3 uses Gemini, so use the same separate environment as the homework.

From the `session3` folder:

```bash
python3 -m venv .venv_homework
source .venv_homework/bin/activate
pip install -r requirements-homework.txt
```

Windows PowerShell:

```powershell
python -m venv .venv_homework
.venv_homework\Scripts\Activate.ps1
pip install -r requirements-homework.txt
```

Download the dataset:

```bash
hf download Birkbeck/les-miserables-txt les_miserables.txt \
  --repo-type dataset \
  --local-dir .
```

Set your Gemini API key in the same terminal where you will run Python.

Replace `PASTE_YOUR_KEY_HERE` with your real key. Do not include spaces around `=`.

```bash
export GEMINI_API_KEY="PASTE_YOUR_KEY_HERE"
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY_HERE"
```

Check that Python can see it:

```bash
python3 -c 'import os; print("GEMINI_API_KEY set:", bool(os.getenv("GEMINI_API_KEY")))'
```

Windows PowerShell:

```powershell
python -c "import os; print('GEMINI_API_KEY set:', bool(os.getenv('GEMINI_API_KEY')))"
```

#### 3. Connect to iterators

Before Gemini, remember that a file object is already an iterator.

```python
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    first_line = next(file)
    second_line = next(file)

print(first_line)
print(second_line)
```

This reads only the first two lines. It does not load the whole book into memory.

You can also loop over the file:

```python
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
        break
```

That loop is streaming. Python gives you one line at a time.

#### 4. Connect to `yield`

`yield` lets us create our own iterator.

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

This generator is useful because it hides the file-reading details. The rest of the program can simply ask for the next useful line.

For RAG, this matters because we often do not want the whole document. We want a small useful chunk.

#### 5. Tiny RAG demo

Create:

```txt
session3/solutions/exercise-03-03.py
```

Copy this code:

```python
import os

from google import genai


TEXT_FILE = "les_miserables.txt"
QUESTION = "Who is Bishop Myriel?"
KEYWORDS = ["bishop", "myriel", "digne"]
MAX_LINES = 8


def useful_lines(path):
    """Yield non-empty lines from a text file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


def retrieve_context(path, keywords, max_lines):
    """Find a small chunk of text that matches the question."""
    matches = []
    extra_lines = 0

    for line in useful_lines(path):
        line_lower = line.lower()

        if any(keyword in line_lower for keyword in keywords):
            matches.append(line)
            # Keep two lines after a match so Gemini has a little context.
            extra_lines = 2
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines:
            break

    return "\n".join(matches)


context = retrieve_context(TEXT_FILE, KEYWORDS, MAX_LINES)

# Send only the retrieved context to Gemini.
prompt = f"""Use only this context to answer the question.

Question:
{QUESTION}

Context:
{context}
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
```

Run:

```bash
python3 solutions/exercise-03-03.py
```

#### 6. What is happening?

This is RAG in its simplest form:

1. `useful_lines()` streams the book and yields one non-empty line at a time.
2. `retrieve_context()` keeps lines that mention `bishop`, `myriel`, or `digne`.
3. It also keeps a couple of lines after each match for context.
4. The retrieved text becomes the context in the prompt.
5. Gemini answers using that context.

The generator keeps the reading logic small and reusable. It also means the program can stop once it has enough context.

#### 7. Why not load the whole book?

You could do this:

```python
with open("les_miserables.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

That loads the whole file into memory. Sometimes that is fine, but it is not the habit we want for large files.

For this task, streaming is enough:

```python
for line in useful_lines("les_miserables.txt"):
    if "myriel" in line.lower():
        print(line)
        break
```

This can stop as soon as it finds useful text.

#### 8. Exercise

Change the question and keywords.

Try this:

```python
QUESTION = "Who is Fantine?"
KEYWORDS = ["fantine"]
```

Then run:

```bash
python3 solutions/exercise-03-03.py
```

Answer these questions in a few lines under your code:

```python
# 1. Which lines were retrieved?
# 2. Did Gemini have enough context?
# 3. What would improve this tiny RAG system?
```

#### 9. Small improvement exercise

At the moment, the script stops when it has 8 matching/context lines.

Try giving Gemini a little more context e.g. 14 lines. Run the script again and compare the answer.

Questions:

- Did Gemini give a more detailed answer?
- What is the trade-off of sending more context?

#### 10. Reflection Task

Write a short reflection, around 150-250 words. Answer these questions:

1. In your own words, what is RAG?
2. What is the context window? Why can we not always send a whole book, website, or dataset to an LLM?
3. How do iterators and `yield` help us build the context gradually instead of loading everything at once?
4. What is one trade-off between sending more context and sending less context to Gemini?

Hint: Think about answer quality, missing useful evidence, prompt length, cost, and noise.

Use this small use case in your answer:

```txt
A student has 50 lecture transcripts and wants to ask:
"What did we say about dynamic programming?"
```

Explain how a simple RAG system could:

1. stream through the transcript files,
2. retrieve only chunks that mention useful keywords,
3. put those chunks into the prompt,
4. ask Gemini for an answer.

Also explain one possible problem. For example, the system might retrieve too little context and miss the answer, or retrieve too much context and make the prompt noisy or expensive.

Post your answer: [Reflection and Homework forum](https://teams.microsoft.com/l/channel/19%3A3c09f9a3815549c0ba1ffd5b12fe7826%40thread.tacv2/Reflection%20and%20Homework?groupId=8b3672d8-2c38-4134-9725-3b779f03c2b0&tenantId=89d07f47-d258-463c-8700-635ffaeca38e)
