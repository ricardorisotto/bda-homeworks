### Session 3 | Homework

> In this homework, you will use `yield` to split *Les Misérables* into small chunks and summarize those chunks with Gemini.

#### 1. Goal

In Session 2, Gemini helped fill missing data. This time, you will use Gemini to summarize chunks of a large text file.

You will:

- use a generator with `yield` to stream book chunks
- avoid loading the whole book into memory
- send one small chunk at a time to Gemini
- compare generator memory use with `readlines()`

#### 2. Prerequisites

The Gemini package and the quiz package currently need different `websockets` versions, so use a separate homework environment.

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

Download the dataset if you do not already have it:

```bash
hf download Birkbeck/les-miserables-txt les_miserables.txt \
  --repo-type dataset \
  --local-dir .
```

#### 3. Set Gemini API key

Set your API key:

```bash
export GEMINI_API_KEY="PASTE_YOUR_KEY"
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY"
```

Quick check:

```bash
python3 -c 'import os; k=os.getenv("GEMINI_API_KEY"); print("GEMINI_API_KEY set:", bool(k)); print("Key length:", len(k) if k else 0)'
```

#### 4. Exercise: summarize book chunks with Gemini

Create:

```txt
session3/solutions/exercise-03-02.py
```

Use the `google-genai` package. Copy this skeleton into `session3/solutions/exercise-03-02.py`.

This exercise uses `yield` to split the book into small chunks. A generator created with `yield` is still an iterator, but it is easier to write than a manual iterator class and it avoids loading the whole book into memory.

```python
import os

from google import genai


MODEL_NAME = "gemini-2.5-flash"
TEXT_FILE = "les_miserables.txt"
CHUNK_SIZE = 30
MAX_CHUNKS = 3


def ask_gemini(prompt):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text


def book_chunks(path, chunk_size=30, max_chunks=3):
    chunk = []
    chunks_sent = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            # Provide here your solution
            ...

    # Provide here your solution
    ...


def build_summary_prompt(chunk_text, chunk_number):
    # Provide here your solution
    ...


for chunk_number, chunk_text in enumerate(
    book_chunks(TEXT_FILE, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS),
    start=1,
):
    prompt = build_summary_prompt(chunk_text, chunk_number)
    summary = ask_gemini(prompt)
    print(f"Chunk {chunk_number}")
    print(summary)
    print()
```

#### 5. Prompt format

Build small chunks using streaming. Do not send the whole book in one request.

Your prompt should ask for this strict output format:

```txt
You are summarizing one chunk from Les Misérables.

Return only valid JSON with these keys:
- chunk: the chunk number
- characters: important character names mentioned
- events: short event descriptions
- summary: a 2-3 sentence summary
- uncertainty: anything unclear

Excerpt:
PASTE_CHUNK_HERE
```

#### 6. Homework tasks

1. Write `book_chunks()` using `yield`.
2. Each chunk should contain about 30 non-empty lines.
3. Stop after 3 chunks so you do not hit API limits.
4. Build one Gemini prompt per chunk.
5. Print each chunk summary.
6. Do not send the whole text file.

#### 7. Complexity discussion

Why this is useful:

- Loading the whole book with `readlines()` uses O(n * m) space.
- A generator with `yield` keeps only the current chunk, so extra space is O(k * m), where `k` is chunk size.
- Total local reading time is still O(n * m) if you process the whole book.
- The improvement is memory usage and start-up time: Gemini can start after the first chunk instead of waiting for the full book to load.

Important comparison:

| Method | Time if all text is processed | Extra space | Why use it? |
|---|---:|---:|---|
| `readlines()` | O(n * m) | O(n * m) | Simple, but loads the whole book |
| Manual iterator class | O(n * m) | O(k * m) | Streams chunks, but more code |
| Generator with `yield` | O(n * m) | O(k * m) | Streams chunks with cleaner code |

So `yield` is not magically faster than every iterator. It is a Pythonic way to write an iterator. The big complexity improvement is avoiding `readlines()` and keeping only one chunk in memory.

> [!TIP]
>
> Show one possible Gemini chunk-summary solution.
>
> <details>
> <summary>Show answer</summary>
>
> ```python
> import os
>
> from google import genai
>
>
> MODEL_NAME = "gemini-2.5-flash"
> TEXT_FILE = "les_miserables.txt"
> CHUNK_SIZE = 30
> MAX_CHUNKS = 3
>
>
> def ask_gemini(prompt):
>     client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
>     response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
>     return response.text
>
>
> def book_chunks(path, chunk_size=30, max_chunks=3):
>     chunk = []
>     chunks_sent = 0
>
>     with open(path, "r", encoding="utf-8") as file:
>         for line in file:
>             line = line.strip()
>             if line == "":
>                 continue
>
>             chunk.append(line)
>
>             if len(chunk) == chunk_size:
>                 yield "\n".join(chunk)
>                 chunks_sent += 1
>                 chunk = []
>
>                 if chunks_sent == max_chunks:
>                     return
>
>     if chunk and chunks_sent < max_chunks:
>         yield "\n".join(chunk)
>
>
> def build_summary_prompt(chunk_text, chunk_number):
>     return f"""You are summarizing one chunk from Les Misérables.
>
> Return only valid JSON with these keys:
> - chunk: the chunk number
> - characters: important character names mentioned
> - events: short event descriptions
> - summary: a 2-3 sentence summary
> - uncertainty: anything unclear
>
> Rules:
> - Do not include Markdown fences.
> - Do not add commentary outside the JSON.
> - If there are no clear events, use an empty list.
>
> Chunk number: {chunk_number}
>
> Excerpt:
> {chunk_text}
> """
>
>
> for chunk_number, chunk_text in enumerate(
>     book_chunks(TEXT_FILE, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS),
>     start=1,
> ):
>     prompt = build_summary_prompt(chunk_text, chunk_number)
>     summary = ask_gemini(prompt)
>     print(f"Chunk {chunk_number}")
>     print(summary)
>     print()
> ```
>
> Reading and chunking the book locally is O(n * m) if all chunks are processed.
>
> Extra space is O(k * m), where `k` is the chunk size. This is better than O(n * m) for loading the whole book.
>
> Gemini API calls are remote black-box time. They depend on network, model, number of chunks, and prompt length.
>
> </details>

#### 8. Reflection

Answer in your notes:

1. Which tasks were best solved with streaming?
2. Which tasks required loading all data?
3. Why is a generator with `yield` still an iterator?
4. When does `yield` save memory compared with `readlines()`?
5. Why is sending the whole book to Gemini in one prompt a bad idea?
