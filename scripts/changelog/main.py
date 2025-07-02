import sys
from datetime import datetime
from git_utils import get_changed_files_and_messages
from changelog_writer import write_changelog
from meta_parser import parse_topics_from_meta
from version_utils import get_version


def categorize_change(file_path: str, message: str) -> str:
    lower_msg = message.lower()
    lower_path = file_path.lower()

    if "delete" in lower_msg or "remove" in lower_msg:
        return "removed"
    elif "add" in lower_msg or "initial" in lower_msg:
        return "added"
    elif "fix" in lower_msg or "bug" in lower_msg:
        return "fixed"
    elif "refactor" in lower_msg:
        return "changed"
    elif "security" in lower_msg:
        return "security"
    elif "deprecate" in lower_msg:
        return "deprecated"
    else:
        if "challenges/" in lower_path:
            return "changed"
        return "changed"


def main():
    args = sys.argv[1:]
    mode = args[0] if args else "unreleased"
    version = args[1] if len(args) > 1 else get_version()
    date = datetime.today().strftime("%Y-%m-%d")

    file_to_message = get_changed_files_and_messages()

    changes = {
        "added": [],
        "changed": [],
        "removed": [],
        "fixed": [],
        "deprecated": [],
        "security": []
    }

    for file_path, message in file_to_message.items():
        category = categorize_change(file_path, message)
        entry = f"- `{file_path}`: {message}"

        if file_path.startswith("challenges/"):
            topics = parse_topics_from_meta(file_path)
            if topics:
                entry += f" _(Topics: {', '.join(topics)})_"

        changes[category].append(entry)

    write_changelog(version, date, changes, mode)


if __name__ == "__main__":
    main()
