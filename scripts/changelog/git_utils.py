import subprocess


def get_changed_files_and_messages():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1"],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = result.stdout.strip().splitlines()
    except subprocess.CalledProcessError:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = result.stdout.strip().splitlines()

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
