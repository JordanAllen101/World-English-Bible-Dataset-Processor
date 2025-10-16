# World English Bible Dataset Processor — Modified Version

A modularized update of the original Cerebras dataset curation scripts, designed to automate and simplify the World English Bible text processing workflow.

This version breaks down the process into easy-to-run steps, eliminating the need to manually copy and paste data between scripts.  
Currently, Steps 1 and 2 are complete — additional steps will be added in future updates.

---

## Description

Originally, this project involved multiple manual text-handling steps to segment the World English Bible into 40-token chunks for dataset training with Cerebras Cloud.  
This modified version  automates and modularizes those steps:

- Step 1 – Packages and preprocesses the input text  
- Step 2 – Cleans and reformats the packaged data for model-ready output  
- Planned – Quality control, over-length handling, and token balancing

---

## Setup Instructions

### 1. Prepare Your Files
Make sure your project directory looks like this:

```
project-folder/
│
├── apikey.txt      # Your Cerebras API key
├── input.txt       # Your source text input
├── first.py        # Step 1: Initial processing
├── output.txt      # Generated after running first.py
├── second.py       # Step 2: Cleaning/formatting
└── README.md
```

### 2. Add Your API Key
Place your Cerebras API key in a file named `apikey.txt`:

```
sk-your_api_key_here
```

### 3. Add Your Input Text
Put your raw text (such as a Bible book) inside `input.txt`.

---

## Usage

### Step 1 — Run Initial Processing
```bash
cd path/to/directory
python first.py
```
This will process the text and output the results into `output.txt`.

### Step 2 — Run Cleaning Script
```bash
python second.py
```
This script reads `output.txt`, cleans or restructures it, and prepares it for further processing or dataset packaging.

---

## About the Original Workflow

This project is derived from David Thrower’s World English Bible Dataset Compilation process, which segments the text into 40-token chunks for training.

**Original workflow included:**
- Manual text packaging  
- Formatting cleanup  
- Quality control for grammar and token limits  
- Handling of over-length samples  

This modified version automates the first two steps, saving time and reducing human error.

---

## Planned Additions
- Step 3: Automated Quality Control  
- Step 4: Over-length Sample Handling  
- Step 5: Exporting formatted datasets  

---

## Requirements
- Python 3.8+  
- cerebras Python SDK  
- Internet access for Cerebras API calls  

Install dependencies:
```bash
pip install cerebras
```

---

## Author
**Modified by:** jordan <stoddardj08@gmail.com>  
**Original framework:** David Thrower <david@cerebros.one>
