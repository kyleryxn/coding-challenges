from datetime import datetime
import subprocess
from pathlib import Path

changelog_path = Path("CHANGELOG.md")
unreleased_header = "## [Unreleased]"

# Configurable list of tracked paths — empty = track all
TRACKED_PATHS = []

def is_tracked(path):
    if not TRACKED_PATHS:
        return True
    return any(path.startswith(p) for p in TRACKED_PATHS)

# Get file changes from latest commit
result = subprocess.run(["git", "diff-tree", "--no-commit-id", "--name-status", "-r", "HEAD"],
                        capture_output=True, text=True)
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

# Classify file changes
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

# Generate new [Unreleased] content
new_unreleased_lines = [unreleased_header]
for section, entries in categories.items():
    if entries:
        new_unreleased_lines.append("")
        new_unreleased_lines.append(f"### {section}")
        for entry in entries:
            new_unreleased_lines.append(f"- `{entry}`")
new_unreleased_block = "\n".join(new_unreleased_lines) + "\n"

# Ensure changelog exists
if not changelog_path.exists():
    changelog_path.write_text("# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n")

content = changelog_path.read_text()

# Split changelog into parts
before = []
after = []
inside_unreleased = False
found_unreleased = False

for line in content.splitlines():
    if line.strip().startswith("## [") and "[Unreleased]" in line:
        found_unreleased = True
        inside_unreleased = True
        before.append(line)  # keep the header to replace
        continue
    elif line.strip().startswith("## [") and inside_unreleased:
        inside_unreleased = False
        after.append(line)
    elif not inside_unreleased:
        (after if found_unreleased else before).append(line)

# If no Unreleased section found, insert it at the top
if not found_unreleased:
    updated = content.strip() + "\n\n" + new_unreleased_block
else:
    updated = "\n".join(before).strip() + "\n\n" + new_unreleased_block + "\n\n" + "\n".join(after).strip()

# Write updated content
changelog_path.write_text(updated + "\n")
print("CHANGELOG.md updated, preserving previous sections.")


# Optional: Function to move [Unreleased] to versioned section with today's date
def release_unreleased(version: str):
    today = datetime.today().strftime("%Y-%m-%d")
    existing = changelog_path.read_text()

    if "## [Unreleased]" not in existing:
        print("No [Unreleased] section found.")
        return

    parts = existing.split("## [Unreleased]")
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

    new_changelog = (
        f"{before}\n\n## [Unreleased]\n\n"
        f"{new_section}\n\n"
        f"{after}"
    )

    changelog_path.write_text(new_changelog.strip() + "\n")
    print(f"[Unreleased] moved to [{version}] dated {today}.")
