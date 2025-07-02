import sys
from datetime import datetime
from git_utils import get_changed_files_and_messages
from changelog_writer import update_changelog
from meta_parser import extract_meta_info
from version_utils import get_version


def categorize_change(file_path: str, message: str) -> str:
    """Categorize the change based on path or message content."""
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
    else:
        # Use location as a fallback
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

        # Optional: enrich with topic metadata
        if file_path.startswith("challenges/"):
            meta_info = extract_meta_info(file_path)
            if meta_info:
                entry += f" _(Topics: {', '.join(meta_info['topics'])})_"

        if category in changes:
            changes[category].append(entry)
        else:
            changes["changed"].append(entry)

    update_changelog(version, date, changes, mode)


if __name__ == "__main__":
    main()
