from datetime import datetime
import subprocess
from pathlib import Path

changelog_path = Path("CHANGELOG.md")
unreleased_header = "## [Unreleased]"

# Use git diff-tree for last commit (reliable in CI)
result = subprocess.run(["git", "diff-tree", "--no-commit-id", "--name-status", "-r", "HEAD"], capture_output=True, text=True)
lines = result.stdout.strip().splitlines()

# Debug output
print("Raw git diff-tree output:")
print(result.stdout)

# Initialize change categories
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
    if not (path.startswith("challenges/") or path == "generate_readme.py"):
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

content = changelog_path.read_text()

# Ensure [Unreleased] section exists
if unreleased_header not in content:
    content += f"\n{unreleased_header}\n"

lines = content.splitlines()

# Ensure all section headers exist
def ensure_section(section):
    header = f"### {section}"
    if header not in lines:
        idx = lines.index(unreleased_header) + 1
        lines.insert(idx, "")
        lines.insert(idx + 1, header)

for section in categories:
    ensure_section(section)

# Insert entries into the correct section
def insert_entries(section, entries):
    header = f"### {section}"
    idx = lines.index(header) + 1
    for entry in entries:
        formatted = f"- `{entry}`"
        if formatted not in lines:
            lines.insert(idx, formatted)
            idx += 1

for section, entries in categories.items():
    insert_entries(section, entries)

# Save updated changelog
changelog_path.write_text("\n".join(lines) + "\n")
print("CHANGELOG.md updated with full Keep a Changelog sections.")
