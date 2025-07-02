from pathlib import Path
from datetime import date

CHANGELOG_PATH = Path("CHANGELOG.md")

def parse_existing():
    return CHANGELOG_PATH.read_text().splitlines() if CHANGELOG_PATH.exists() else []

def write_changelog(version, changes):
    today = date.today().isoformat()
    header = f"## [{version}] - {today}\n"
    sections = ""

    if changes["added"]:
        sections += "### Added\n" + "\n".join(changes["added"]) + "\n\n"
    if changes["changed"]:
        sections += "### Changed\n" + "\n".join(changes["changed"]) + "\n\n"

    previous = parse_existing()
    with open(CHANGELOG_PATH, "w") as f:
        f.write(header + "\n" + sections + "\n")
        f.write("\n".join(previous))
