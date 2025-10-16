samples = [line.strip() for line in open("output.txt", "r", encoding="utf-8")]



from transformers import AutoTokenizer
tokenizer_checkpoint = "HuggingFaceTB/SmolLM3-3B" # "HuggingFaceTB/SmolLM2-1.7B-Instruct" 
tokenizer = AutoTokenizer.from_pretrained(tokenizer_checkpoint)

print(f"Number of Samples: {len(samples)}")
tokens = [tokenizer(sample)['input_ids'] for sample in samples]


import numpy as np
sample_word_counts = np.array([len(a) for a in tokens])
print(f"max len: {sample_word_counts.max()}")
print(f"min len: {sample_word_counts.min()}")
print(f"mean len: {sample_word_counts.mean()}")
print(f"len std: {sample_word_counts.std()}")
print(f"num over token count: {np.array(sample_word_counts > 40).sum()}")
# print("NEW SAMPLE:")
# samples_np = np.array(samples, dtype=object)
# print([str(x) for x in samples_np[sample_word_counts <= 40].tolist()])

