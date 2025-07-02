# scripts/changelog/main.py

from datetime import datetime
from version_utils import get_version
from git_utils import get_changed_files_and_messages
from meta_parser import parse_topics_from_meta
from changelog_writer import write_changelog

def group_changes_by_type(changes: dict[str, str]) -> dict[str, list[str]]:
    grouped = {
        "added": [],
        "changed": [],
        "removed": [],
        "fixed": [],
        "deprecated": [],
        "security": []
    }

    for path, message in changes.items():
        lower_msg = message.lower()
        entry = f"- `{path}`: {message}"

        # Only add topics if it's a challenge file
        topics = parse_topics_from_meta(path)
        if topics:
            entry += f" _(Topics: {', '.join(topics)})_"

        if any(keyword in lower_msg for keyword in ["fix", "bug"]):
            grouped["fixed"].append(entry)
        elif any(keyword in lower_msg for keyword in ["remove", "delete"]):
            grouped["removed"].append(entry)
        elif any(keyword in lower_msg for keyword in ["add", "initial"]):
            grouped["added"].append(entry)
        elif any(keyword in lower_msg for keyword in ["deprecate"]):
            grouped["deprecated"].append(entry)
        elif any(keyword in lower_msg for keyword in ["security", "vulnerability"]):
            grouped["security"].append(entry)
        else:
            grouped["changed"].append(entry)

    return grouped

def main(mode="unreleased"):
    version = get_version()
    date = datetime.today().strftime("%Y-%m-%d")

    changes = get_changed_files_and_messages()
    if not changes:
        print("No relevant file changes detected.")
        return

    grouped = group_changes_by_type(changes)

    print("Changes grouped by type:")
    for k, v in grouped.items():
        if v:
            print(f"\n### {k.upper()}")
            for entry in v:
                print(entry)

    write_changelog(version, date, grouped, mode)

if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else "unreleased"
    main(arg)
