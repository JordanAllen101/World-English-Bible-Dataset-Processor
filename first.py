import os, sys
from cerebras.cloud.sdk import Cerebras

# Read API key
with open("apikey.txt", "r", encoding="utf-8") as f:
    api_key = f.read()
client = Cerebras(api_key=api_key)

MODEL = "qwen-3-coder-480b"
MAX_SEQ_LEN = 30

# Read input text
with open("input.txt", "r", encoding="utf-8") as f:
    RAW_TEXT = f.read()

# Build prompt
PROMPT = (
    "\nPlease package the data below to train an LLM for non-instruct text completion.\n\n"
    "1. Context length summarization (not truncation) to proof-of-concept scale of NO MORE THAN " + str(MAX_SEQ_LEN) + " tokens per sample.\n"
    "2 Strip anything that is not English prose: citations, URLs, line wraps, stray Unicode, labels, page numbers, verse numbers, etc.\n"
    "3. Ensure that samples begin with proper capitalization, end with correct punctuation, and end naturally.\n"
    "4. Return plain lines of text, one complete thought per line.\n"
    "5. Do not include quotes, commas, or any list formatting.\n"
    "6. Process the entire input text.\n\n"
    "Text:\n" + RAW_TEXT + "\n"
)

# Call the model
completion_response = client.chat.completions.create(
    messages=[{"role": "user", "content": PROMPT}],
    model=MODEL,
    stream=False,
    max_completion_tokens=20000,
    temperature=0.7,
    top_p=0.8
)

# Extract model output
model_output = completion_response.choices[0].message.content

# Split into lines, remove empty lines
lines = [line.strip() for line in model_output.splitlines() if line.strip()]

# Save lines to output.txt as plain text
with open("output.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print(f"Model output written to output.txt with {len(lines)} plain-text lines.")
