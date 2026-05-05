"""Session 3 Exercise 3 reference solution: smallest RAG demo with Gemini.

Run from the session3 folder:
    python3 session_solutions/exercise-03-03.py

Before running:
    pip install -r requirements-homework.txt
    export GEMINI_API_KEY="PASTE_YOUR_KEY"
    hf download Birkbeck/les-miserables-txt les_miserables.txt --repo-type dataset --local-dir .
"""

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
