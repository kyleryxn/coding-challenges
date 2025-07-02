from pathlib import Path
from datetime import date

CHANGELOG_PATH = Path("CHANGELOG.md")

STATIC_HEADER = """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
"""

def parse_existing():
    if CHANGELOG_PATH.exists():
        return CHANGELOG_PATH.read_text().splitlines()
    return []

def write_changelog(version, changes):
    today = date.today().isoformat()
    version_header = f"## [{version}] - {today}"

    # Assemble version section
    version_lines = [version_header, ""]
    if changes["added"]:
        version_lines.append("### Added")
        version_lines.extend(changes["added"])
        version_lines.append("")
    if changes["changed"]:
        version_lines.append("### Changed")
        version_lines.extend(changes["changed"])
        version_lines.append("")

    version_block = "\n".join(version_lines)

    existing = parse_existing()
    existing_content = "\n".join(existing)

    if existing_content.startswith("# Changelog"):
        # Remove existing version if duplicated
        existing_versions = existing_content.split("## [")
        preserved_header = STATIC_HEADER.strip()
        rest = ["## [" + v for v in existing_versions[1:]] if len(existing_versions) > 1 else []
        existing_body = "\n".join(rest).strip()
    else:
        preserved_header = STATIC_HEADER.strip()
        existing_body = existing_content.strip()

    # Assemble final changelog
    new_content = f"{preserved_header}\n\n{version_block}\n\n{existing_body}".strip()
    CHANGELOG_PATH.write_text(new_content + "\n")
    print(f"✅ CHANGELOG.md updated for version {version}")
