import os

from google import genai


TEXT_FILE = "les_miserables.txt"
QUESTION = "Who is Fantine?"
KEYWORDS = ["fantine"]
MAX_LINES = 14


def useful_lines(path):
    """Yield non-empty lines from a text file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

def count_useful_lines(path):
    return sum(1 for _ in useful_lines(path))

def retrieve_context(path, keywords, max_lines):
    """Find a small chunk of text that matches the question."""
    matches = []
    extra_lines = 0
    line_number = 0

    for line in useful_lines(path):
        line_lower = line.lower()
        line_number += 1

        if any(keyword in line_lower for keyword in keywords):
            matches.append(line)
            # Keep two lines after a match so Gemini has a little context.
            extra_lines = 2
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines:
            break

    print(f"Found {len(matches)} matching lines in {line_number} lines before reaching a limit on context size.")        

    return "\n".join(matches)

print(f"Total useful lines in the file: {count_useful_lines(TEXT_FILE)}")

context = retrieve_context(TEXT_FILE, KEYWORDS, MAX_LINES)

print("Context retrieved:")
print(context)
print("\nHere's the answer from Gemini:\n") 

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