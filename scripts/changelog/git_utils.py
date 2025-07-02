import subprocess

IGNORED_PATTERNS = [
    ".github/",
    ".yml",
    ".yaml",
    "CHANGELOG.md",
    "version.txt",
]

def is_meaningful_file(file):
    return not any(pattern in file for pattern in IGNORED_PATTERNS)


def get_changed_files_and_messages():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1"],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = [f for f in result.stdout.strip().splitlines() if is_meaningful_file(f)]
    except subprocess.CalledProcessError:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = [f for f in result.stdout.strip().splitlines() if is_meaningful_file(f)]

    file_to_message = {}
    for file in changed_files:
        try:
            message_result = subprocess.run(
                ["git", "log", "-1", "--pretty=%s", file],
                capture_output=True,
                text=True,
                check=True
            )
            message = message_result.stdout.strip()
        except subprocess.CalledProcessError:
            message = "Updated"
        file_to_message[file] = message

    return file_to_message
