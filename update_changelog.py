from datetime import datetime
import subprocess
from pathlib import Path

changelog_path = Path("CHANGELOG.md")
unreleased_header = "## [Unreleased]"

# Get changed files from last commit
result = subprocess.run(["git", "diff", "--name-only", "HEAD~1"], capture_output=True, text=True)
changed_files = result.stdout.strip().splitlines()

# Only include relevant tracked files
relevant_files = [f for f in changed_files if f.startswith("challenges/") or f == "generate_readme.py"]

if not relevant_files:
    print("No relevant changes to log.")
    exit(0)

# Load or initialize the changelog
if not changelog_path.exists():
    changelog_path.write_text("# 📋 Changelog\n\nAll notable changes to this project will be documented in this file.\n"
    "\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).")

content = changelog_path.read_text()

# Ensure Unreleased section exists
if unreleased_header not in content:
    content += f"\n{unreleased_header}\n\n### Changed\n"

# Split content into lines for insertion
lines = content.splitlines()

# Insert changed files under 'Changed'
insert_index = -1
for i, line in enumerate(lines):
    if line.strip() == "### Changed":
        insert_index = i + 1
        break

# Insert new entries only if they aren't already there
for file in relevant_files:
    entry = f"- `{file}`"
    if entry not in lines:
        lines.insert(insert_index, entry)
        insert_index += 1

# Rewrite the changelog
changelog_path.write_text("\n".join(lines) + "\n")
print("✅ CHANGELOG.md updated using Keep a Changelog format.")
