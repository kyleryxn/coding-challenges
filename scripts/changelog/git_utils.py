from subprocess import run, PIPE
import os

def get_changed_files_and_messages():
    # Fetch full commit history for GitHub Actions
    run(["git", "fetch", "--unshallow"], stdout=PIPE, stderr=PIPE)

    # Get all commits in this push (from the second-last version tag)
    result = run(["git", "rev-list", "--tags", "--max-count=1"], stdout=PIPE, text=True)
    last_tag = result.stdout.strip() or "HEAD~10"  # fallback to last 10 commits

    diff_result = run(["git", "log", "--pretty=format:%H", f"{last_tag}..HEAD"], stdout=PIPE, text=True)
    commits = diff_result.stdout.strip().splitlines()

    file_to_message = {}

    for commit_hash in commits:
        # Get files changed in this commit
        diff_files = run(["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash],
                         stdout=PIPE, text=True).stdout.strip().splitlines()

        message = run(["git", "log", "-1", "--pretty=%s", commit_hash], stdout=PIPE, text=True).stdout.strip()

        for f in diff_files:
            if f.endswith(".py") or f.startswith("challenges/"):  # Filter scope
                file_to_message[f] = message

    return file_to_message
