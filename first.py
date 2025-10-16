import os, sys
from cerebras.cloud.sdk import Cerebras
with open("apikey.txt", "r", encoding="utf-8") as f:
    api_key = f.read()
client = Cerebras(
    api_key=api_key
)

MODEL = "qwen-3-coder-480b"  # "qwen-3-235b-a22b-instruct-2507"
MAX_SEQ_LEN = 30

with open("input.txt", "r", encoding="utf-8") as f:
    RAW_TEXT = f.read()

PROMPT = (
    "\nPlease package the data below o train an LLM for non-instruct text completion.\n\n"
    "1. Context length summarization (not truncation) to proof-of-concept scale of **NO MORE THAN** " + str(MAX_SEQ_LEN) + " tokens per sample.\n"
    "2 Strip anything that is not English prose: Citations, URLs, line wraps, stray Unicode, labels, page numbers, verse numbers, etc.\n"
    "3 Ensuring that samples begin with proper capitalization, end with correct punctuation and a natural end of paragraph, **not just naively truncating sequential sentences in the text** as separate samples that end “mid - paragraph” … which would have the undesired effect of encouraging the model to write in a verbose format beyond the context window and terminate its writings mid paragraph / throw a stop token without expressing a complete thought.\n"
    "4. Package as a Python list[str].\n"
    "5. Make no comments like \"here is the data packaged as requested\". Simply return a Python list[str] as described.\n"
    "6. Process the entire data provided, as described.\n\n"
    "This is the data to package.\n\n"
    "```text\n" + RAW_TEXT + "\n```\n\n"
)

completion_create_response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": PROMPT
        }
    ],
    model=MODEL,
    stream=False,
    max_completion_tokens=20000,
    temperature=0.7,
    top_p=0.8
)

# Extract only the model's generated text
model_output = completion_create_response.choices[0].message.content

# Print the text
print(model_output)

# Save only the text to a file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(model_output)

print("Model output written to output.txt")
