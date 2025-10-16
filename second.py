import numpy as np
from transformers import AutoTokenizer

# -----------------------------
# Initialize empty list
# -----------------------------
samples = []

# -----------------------------
# Read output.txt line by line and append
# -----------------------------
with open("output.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:  # skip empty lines
            samples.append(line)

# -----------------------------
# Initialize tokenizer
# -----------------------------
tokenizer_checkpoint = "HuggingFaceTB/SmolLM3-3B"  # or your preferred tokenizer
tokenizer = AutoTokenizer.from_pretrained(tokenizer_checkpoint)

# -----------------------------
# Tokenize each sample
# -----------------------------
tokens = [tokenizer(sample)['input_ids'] for sample in samples]

# -----------------------------
# Compute statistics
# -----------------------------
sample_word_counts = np.array([len(t) for t in tokens])

print(f"Number of Samples: {len(samples)}")
print(f"max len: {sample_word_counts.max()}")
print(f"min len: {sample_word_counts.min()}")
print(f"mean len: {sample_word_counts.mean():.2f}")
print(f"len std: {sample_word_counts.std():.2f}")
print(f"num over token count: {np.sum(sample_word_counts > 40)}")

