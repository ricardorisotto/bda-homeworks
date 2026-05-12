import os

from google import genai


MODEL_NAME = "gemini-2.5-flash"
TEXT_FILE = "les_miserables.txt"
CHUNK_SIZE = 30
MAX_CHUNKS = 3
PROMPT_TEMPLATE = f"You are summarizing a chunk of text. \n\
Return only valid JSON with these keys: \n\
- chunk: the chunk number \n\
- characters: important character names mentioned \n\
- events: short event descriptions \n\
- summary: a 2-3 sentence summary\n \
- uncertainty: anything unclear \n\
\n\
Here is the chunk number and the chunk of text to summarize: \
Chunk number {{chunk_number}} \n \
Chunk of text: {{chunk_text}}"



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
            if len(chunk) < chunk_size:
                chunk.append(line)
            else:
                # convert the chunk to a single string with lines separated by newlines 
                # and yield it
                chunk_text = "\n".join(chunk)
                chunks_sent += 1
                print(f"Yielding chunk {chunks_sent} with {len(chunk)} lines:\n{chunk_text}\n")
                yield chunk_text
                # Note that this code below continues after the yield, 
                # so it will only run after the chunk has been sent to Gemini.

                # Stop if we've reached the maximum number of chunks.
                if chunks_sent >= max_chunks:
                    print(f"Reached the maximum number of chunks ({max_chunks}). Stopping.")
                    return
                
                # Else start a new chunk with the current line.
                chunk = [line]
                
                

    print(f"Finished reading the file. Total chunks sent: {chunks_sent}.")    



              




def build_summary_prompt(chunk_text, chunk_number):
    # Provide here your solution
    return PROMPT_TEMPLATE.format(chunk_number=chunk_number, chunk_text=chunk_text) 


for chunk_number, chunk_text in enumerate(
    book_chunks(TEXT_FILE, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS),
    start=1,
):
    prompt = build_summary_prompt(chunk_text, chunk_number)
    print(f"Prompt for chunk {chunk_number}:\n{prompt}\n")
    summary = ask_gemini(prompt)
    print(f"Chunk {chunk_number}")
    print(summary)
    print()