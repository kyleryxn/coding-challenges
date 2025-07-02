from git_utils import get_changed_paths, get_commit_messages
from meta_parser import parse_topics_from_meta
from changelog_writer import write_changelog
from version_utils import get_version

def main():
    version = get_version()
    changed_paths = get_changed_paths()
    commit_messages = get_commit_messages()

    print("Changed paths:")
    for path in changed_paths:
        print(f"- {path}")

    print("\nCommit messages:")
    for msg in commit_messages:
        print(f"- {msg}")

    # Create a dictionary of changes per file with topic info (if available)
    changes = []
    for path in changed_paths:
        topics = parse_topics_from_meta(path)
        changes.append({
            "file": path,
            "topics": topics
        })

    write_changelog(version, changes, commit_messages)

if __name__ == "__main__":
    main()
