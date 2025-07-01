import json
from pathlib import Path

# Define the coding challenges root directory and the README path
root_dir = Path(__file__).parent
readme_path = root_dir / "README.md"

# Define function to detect languages from solution file extensions
EXTENSION_LANG_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust"
}

def detect_languages(folder_path):
    languages = set()
    for file in folder_path.glob("solution.*"):
        lang = EXTENSION_LANG_MAP.get(file.suffix)
        if lang:
            languages.add(lang)
    return sorted(languages)

# Build problem index entries
index_entries = []

for problem_folder in sorted(root_dir.iterdir()):
    if problem_folder.is_dir():
        meta_file = problem_folder / "meta.json"
        if meta_file.exists():
            with open(meta_file) as f:
                meta = json.load(f)
            source = meta.get("source", "Unknown")
        else:
            source = "Unknown"

        languages = detect_languages(problem_folder)
        languages_str = ", ".join(languages) if languages else "—"
        entry = f"| [{problem_folder.name}](./{problem_folder.name}) | {languages_str} | {source} |"
        index_entries.append(entry)

# Create README content
readme_content = f"""# 🧠 Coding Challenge Solutions Repository

Welcome to my personal archive of coding challenge solutions!  
This repository centralizes solutions across multiple platforms like **LeetCode**, **HackerRank**, and **job application assessments**, organized **by problem name**, with implementations in **multiple programming languages**.

---

## 📁 Structure

Each folder in the repo corresponds to **one problem**, and contains:
- `README.md`: Problem description, source link, and notes  
- `solution.<lang>`: One or more solutions in different programming languages  
- Optional explanations or test files

Example:

```
TwoSum/
├── README.md
├── solution.java
├── solution.py
└── solution.cpp
```

---

## ✅ Problem Index

| Problem | Languages | Source(s) |
|---------|-----------|-----------|
{chr(10).join(index_entries)}

> 🛠️ *This table is auto-generated from `meta.json` files and solution filenames.*

---

## 🧭 Goals

- Improve mastery of **data structures and algorithms**
- Prepare for **technical interviews**
- Track progress across **platforms and companies**
- Reinforce learning by comparing solutions in **multiple languages**

---

## 🛠️ Languages Used

- `Java`
- `Python`
- `C++`
- (Coming soon: JavaScript, Go, Rust...)

---

## 🔍 Tags to Consider Adding

In future versions, tags may help with searching:
- `#array`, `#hashmap`, `#greedy`, `#dp`, `#binarysearch`, `#slidingwindow`
- `#leetcode`, `#hackerrank`, `#interview`

---

## ✍️ License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---
"""

# Write the generated README.md
readme_path.write_text(readme_content)
print("README.md has been successfully regenerated.")
