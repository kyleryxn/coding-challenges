import json
from pathlib import Path

root_dir = Path("challenges")
readme_path = Path("README.md")

if not root_dir.exists():
    raise FileNotFoundError(f"Expected folder '{root_dir}/' not found in the repo root.")

EXTENSION_LANG_MAP = {
    ".c": "C",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".java": "Java",
    ".js": "JavaScript",
    ".py": "Python",
    ".rs": "Rust",
    ".ts": "TypeScript"
}

def detect_languages(folder_path):
    return sorted({
        EXTENSION_LANG_MAP.get(file.suffix)
        for file in folder_path.glob("solution.*")
        if EXTENSION_LANG_MAP.get(file.suffix)
    })

index_entries = []

for problem_folder in sorted(root_dir.iterdir(), key=lambda p: p.name.lower()):
    if problem_folder.is_dir():
        meta = {}
        meta_file = problem_folder / "meta.json"

        if meta_file.exists():
            with open(meta_file) as f:
                meta = json.load(f)

        source = meta.get("source", "Unknown")
        languages = detect_languages(problem_folder)
        lang_str = ", ".join(languages) if languages else "—"
        topics = meta.get("topics", "Unknown")
        topics_str = ", ".join(topics)
        problem_folder_str = problem_folder.name.replace("-", " ").title()

        index_entries.append(f"| [{problem_folder_str}](./challenges/{problem_folder.name}) | {lang_str} | {source} | {topics_str}")

readme_content = f"""# 🧠 Coding Challenge Encyclopedia

Centralized solutions to coding challenges from LeetCode, HackerRank, job interviews, and other sources.  
Organized by **problem name**, with **multiple languages supported**.


## 📁 Structure

Each folder contains:
- `meta.json`: Metadata like source, difficulty
- `solution.<ext>`: Solution file(s)
- Optional notes or test cases


## ✅ Problem Index

| Problem | Languages | Source(s) | Topic(s) |
|---------|-----------|-----------|----------|
{chr(10).join(index_entries)}

## 📃 License

[MIT License](./LICENSE.txt)
"""

readme_path.write_text(readme_content)

print("README.md updated.")
