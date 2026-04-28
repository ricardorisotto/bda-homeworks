### Session 2 | Part 1

> In Part 1, you will prepare Gemini API access and run an AI-assisted data-cleaning workflow, then complete a set of quizzes.

#### 1. Goal

You will:

- create a free API key in Google AI Studio
- complete a set of quizzes

#### 2. Prerequisites

Before starting:

1. Open the `session2` folder in Visual Studio Code.
2. Create and activate your virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

#### 3. Create API key (free)

Go to Google AI Studio and create an API key:

- https://aistudio.google.com/app/api-keys
- Add a name (or keep default) and choose `Default Gemini Project`.
- Create a key and keep it private.
- Copy the API key e.g. `AIza...`.

#### 4. Set API key in terminal

On macOS/Linux:

```bash
export GEMINI_API_KEY="PASTE_YOUR_KEY"
```

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY"
```

**Test key is set**

Run this quick check in your terminal:

```bash
python3 -c 'import os; k=os.getenv("GEMINI_API_KEY"); print("GEMINI_API_KEY set:", bool(k)); print("Key length:", len(k) if k else 0)'
```

If `GEMINI_API_KEY set: True` appears and key length is greater than 0, your environment variable is working. Clear your terminal using `clear`, and let's proceed.

**Limits note**

Google AI Studio is free, but it has usage limits (typically 5-15 requests per minute, depending on the model).

> [!TIP]
>
> Limits depend on model and tier, and can change over time. 
>
> Check the latest limits before running: https://ai.google.dev/gemini-api/docs/quota. If you exceed limits, you may receive `429` errors until quota resets.

#### 5. Read quiz instructions first

Before starting the quizzes:

1. Read each question carefully before selecting an answer.
2. For the essay quizzes, answer all parts clearly using Big-O notation when requested.
3. Keep answers concise and practical.

#### 6. Complete the quizzes

Essay quiz:

```bash
quizmd quizzes/python-data-cleaning-tradeoff-essay.md
```

Essay quiz 2:

```bash
quizmd quizzes/python-complexity-basics-essay.md
```

Debug quiz:

```bash
quizmd quizzes/python-session-01-debug-quiz.md
```
