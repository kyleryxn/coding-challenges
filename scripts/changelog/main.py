from pathlib import Path
from git_utils import get_changed_paths, get_commit_message
from changelog_writer import write_changelog
from meta_parser import get_changelog_note

VERSION_PATH = Path("version.txt")

def get_version():
    return VERSION_PATH.read_text().strip()

def classify(path):
    parts = Path(path).parts
    return "added" if parts[0] == "challenges" and len(parts) == 2 else "changed"

def main():
    version = get_version()
    changes = {"added": [], "changed": []}
    seen = set()

    for path in get_changed_paths():
        base = str(Path(path).parent if Path(path).is_file() else path)
        if base in seen:
            continue
        seen.add(base)

        note = get_changelog_note(base) or get_commit_message(path)
        entry = f"- `{base}`" + (f": {note}" if note else "")
        change_type = classify(path)
        changes[change_type].append(entry)

    if changes["added"] or changes["changed"]:
        write_changelog(version, changes)
        print("CHANGELOG.md updated.")
    else:
        print("No relevant changes to log.")

if __name__ == "__main__":
    main()
