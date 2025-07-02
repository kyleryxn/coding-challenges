import json
from pathlib import Path

def get_changelog_note(folder_path):
    meta_file = Path(folder_path) / "meta.json"
    if meta_file.exists():
        try:
            with open(meta_file) as f:
                return json.load(f).get("changelog_note", "")
        except json.JSONDecodeError:
            return ""
    return ""
