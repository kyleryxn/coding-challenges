from pathlib import Path

CHANGELOG_PATH = Path("CHANGELOG.md")


def write_changelog(version: str, date: str, changes: dict, mode: str = "unreleased"):
    if CHANGELOG_PATH.exists():
        existing_lines = CHANGELOG_PATH.read_text().splitlines()
    else:
        existing_lines = []

    header = [
        "# Changelog",
        "",
        "All notable changes to this project will be documented in this file.",
        "",
        "The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),",
        "and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).",
        ""
    ]

    if mode == "release":
        title = f"## [{version}] - {date}"
    else:
        title = "## [Unreleased]"

    body = [title]
    for section in ["added", "changed", "removed", "fixed", "deprecated", "security"]:
        entries = changes.get(section, [])
        if entries:
            body.append(f"### {section.capitalize()}")
            body.extend(entries)
            body.append("")

    body.append("")

    # Remove any previous block with same version/unreleased
    lines = [line for line in existing_lines if not line.startswith(f"## [{version}]") and line != "## [Unreleased]"]
    final = header + body + lines
    CHANGELOG_PATH.write_text("\n".join(final))
