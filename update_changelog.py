from datetime import datetime
import subprocess
from pathlib import Path
import re

changelog_path = Path("CHANGELOG.md")
unreleased_header = "## [Unreleased]"

# Configurable list of tracked paths — empty = track all
TRACKED_PATHS = []

def is_tracked(path):
    if not TRACKED_PATHS:
        return True
    return any(path.startswith(p) for p in TRACKED_PATHS)

# Get file changes in the latest commit
result = subprocess.run(["git", "diff-tree", "--no-commit-id", "--name-status", "-r", "HEAD"], capture_output=True, text=True)
lines = result.stdout.strip().splitlines()
print("Raw git diff-tree output:")
print(result.stdout)

# Initialize changelog categories
categories = {
    "Added": [],
    "Changed": [],
    "Deprecated": [],
    "Removed": [],
    "Fixed": [],
    "Security": []
}

# Classify changes
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
    exit(0)

# Ensure CHANGELOG.md exists
if not changelog_path.exists():
    changelog_path.write_text("# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n")

existing = changelog_path.read_text()

# Generate new Unreleased content
new_unreleased_lines = [unreleased_header]
for section, entries in categories.items():
    if entries:
        new_unreleased_lines.append("")
        new_unreleased_lines.append(f"### {section}")
        for entry in entries:
            new_unreleased_lines.append(f"- `{entry}`")
new_unreleased = "\n".join(new_unreleased_lines) + "\n"

# Replace or insert [Unreleased] section
if unreleased_header in existing:
    pattern = r"## \[Unreleased\](.*?)(?=\n## \[|\Z)"  # non-greedy match until next release or end
    updated = re.sub(pattern, new_unreleased.strip(), existing, flags=re.DOTALL)
else:
    insert_point = existing.find("# Changelog") + len("# Changelog")
    updated = existing[:insert_point] + "\n\n" + new_unreleased + "\n" + existing[insert_point:]

changelog_path.write_text(updated)
print("CHANGELOG.md updated while preserving previous releases.")
