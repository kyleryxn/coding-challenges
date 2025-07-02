import sys
from pathlib import Path

version_file = Path("version.txt")
if not version_file.exists():
    print("version.txt not found.")
    sys.exit(1)

current = version_file.read_text().strip()
major, minor, patch = map(int, current.split("."))

if len(sys.argv) != 2 or sys.argv[1] not in {"major", "minor", "patch"}:
    print("Usage: python bump_version.py [major|minor|patch]")
    sys.exit(1)

if sys.argv[1] == "major":
    major += 1
    minor = 0
    patch = 0
elif sys.argv[1] == "minor":
    minor += 1
    patch = 0
elif sys.argv[1] == "patch":
    patch += 1

new_version = f"{major}.{minor}.{patch}"
version_file.write_text(new_version + "\n")
print(f"Bumped to version {new_version}")
