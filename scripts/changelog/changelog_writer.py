from pathlib import Path

CHANGELOG_PATH = Path("CHANGELOG.md")

def remove_existing_sections(lines, version):
    cleaned = []
    skip = False
    for line in lines:
        if line.startswith(f"## [{version}]") or line.startswith("## [Unreleased]"):
            skip = True
        elif line.startswith("## "):  # next section starts
            skip = False
        if not skip:
            cleaned.append(line)
    return cleaned

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

    cleaned_lines = remove_existing_sections(existing_lines, version)

    # Only add header once
    if cleaned_lines[:len(header)] != header:
        cleaned_lines = header + [""] + cleaned_lines

    final = cleaned_lines[:len(header)] + body + cleaned_lines[len(header):]
    CHANGELOG_PATH.write_text("\n".join(final))
