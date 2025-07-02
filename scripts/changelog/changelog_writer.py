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

    # Preserve the header and any pre-existing entries
    header_end_index = 0
    for i, line in enumerate(existing_lines):
        if line.startswith("## "):
            header_end_index = i
            break

    preserved_header = existing_lines[:header_end_index]
    remaining_log = [
        line for line in existing_lines[header_end_index:]
        if not line.startswith(f"## [{version}]") and line != "## [Unreleased]"
    ]

    final = preserved_header + [""] + body + remaining_log
    CHANGELOG_PATH.write_text("\n".join(final))

