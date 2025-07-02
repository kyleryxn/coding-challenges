from subprocess import run, PIPE, CalledProcessError

def get_changed_paths():
    try:
        result = run(["git", "diff", "--name-only", "HEAD~1"], stdout=PIPE, text=True, check=True)
        return result.stdout.strip().splitlines()
    except CalledProcessError:
        # Fallback: list all tracked files (e.g., on first commit or fresh clone)
        result = run(["git", "ls-files"], stdout=PIPE, text=True, check=True)
        print("⚠️ Warning: HEAD~1 not found — falling back to all tracked files.")
        return result.stdout.strip().splitlines()

def get_commit_message(path):
    try:
        result = run(["git", "log", "-1", "--pretty=%s", "--", path], stdout=PIPE, text=True, check=True)
        return result.stdout.strip()
    except CalledProcessError:
        return ""
