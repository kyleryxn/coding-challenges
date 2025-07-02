import sys
from datetime import datetime
import subprocess
from pathlib import Path

changelog_path = Path("CHANGELOG.md")
unreleased_header = "## [Unreleased]"
TRACKED_PATHS = []  # Empty = track all

def is_tracked(path):
    if not TRACKED_PATHS:
        return True
    return any(path.startswith(p) for p in TRACKED_PATHS)

def update_unreleased_section():
    result = subprocess.run(["git", "diff-tree", "--no-commit-id", "--name-status", "-r", "HEAD"],
                            capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    print("Raw git diff-tree output:")
    print(result.stdout)

    categories = {
        "Added": [],
        "Changed": [],
        "Deprecated": [],
        "Removed": [],
        "Fixed": [],
        "Security": []
    }

    for line in lines:
        if not line.strip():
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            continue
        status, path = parts
        if not is_tracked(path):
            continue
        if status == "A":
            categories["Added"].append(path)
        elif status == "M":
            categories["Changed"].append(path)
        elif status == "D":
            categories["Removed"].append(path)

    if not any(categories.values()):
        print("No relevant changes to log.")
        return

    new_lines = [unreleased_header]
    for section, entries in categories.items():
        if entries:
            new_lines.append("")
            new_lines.append(f"### {section}")
            for entry in sorted(entries):
                new_lines.append(f"- `{entry}`")
    block = "\n".join(new_lines) + "\n"

    if not changelog_path.exists():
        changelog_path.write_text("# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n")

    content = changelog_path.read_text()
    before, after = [], []
    inside_unreleased, found = False, False

    for line in content.splitlines():
        if line.strip().startswith("## [") and "[Unreleased]" in line:
            found = True
            inside_unreleased = True
            before.append(line)
            continue
        elif line.strip().startswith("## [") and inside_unreleased:
            inside_unreleased = False
            after.append(line)
        elif not inside_unreleased:
            (after if found else before).append(line)

    if not found:
        updated = content.strip() + "\n\n" + block
    else:
        updated = "\n".join(before).strip() + "\n\n" + block + "\n\n" + "\n".join(after).strip()

    changelog_path.write_text(updated + "\n")
    print("CHANGELOG.md updated.")

def release_unreleased(version: str):
    today = datetime.today().strftime("%Y-%m-%d")
    content = changelog_path.read_text()

    if "## [Unreleased]" not in content:
        print("No [Unreleased] section found.")
        return

    parts = content.split("## [Unreleased]")
    before = parts[0].rstrip()
    rest = parts[1]

    if "## [" in rest:
        split_point = rest.find("## [", 1)
        unreleased_body = rest[:split_point].strip()
        after = rest[split_point:].lstrip()
    else:
        unreleased_body = rest.strip()
        after = ""

    release_header = f"## [{version}] - {today}"
    new_section = f"{release_header}\n\n{unreleased_body}"

    new_content = (
        f"{before}\n\n## [Unreleased]\n\n"
        f"{new_section}\n\n"
        f"{after}"
    )

    changelog_path.write_text(new_content.strip() + "\n")
    print(f"[Unreleased] moved to [{version}] dated {today}.")

def show_help():
    print("""Usage:
  python update_changelog.py                # Update [Unreleased] section from latest commit
  python update_changelog.py release 1.2.0  # Promote [Unreleased] to versioned release
  python update_changelog.py help           # Show this help message
""")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        update_unreleased_section()
    elif len(sys.argv) == 2 and sys.argv[1] == "help":
        show_help()
    elif len(sys.argv) == 3 and sys.argv[1] == "release":
        release_unreleased(sys.argv[2])
    else:
        print("Invalid usage.\n")
        show_help()
