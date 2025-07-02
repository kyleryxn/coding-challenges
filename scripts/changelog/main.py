from changelog_writer import write_changelog
from git_utils import get_changed_files_and_messages
from meta_parser import parse_meta_for_paths
from version_utils import get_version
import sys
from datetime import date


def main():
    args = sys.argv[1:]

    # Determine version and mode
    version = None
    if args and args[0] == "release":
        version = get_version()
        version_str = f"[{version}] - {date.today()}"
    else:
        version_str = "[Unreleased]"

    # Get changed files and messages
    changes = get_changed_files_and_messages()

    # Parse metadata where applicable
    enriched_changes = parse_meta_for_paths(changes)

    # Write to the changelog
    write_changelog(version_str, enriched_changes)


if __name__ == "__main__":
    main()
