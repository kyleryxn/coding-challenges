from subprocess import run, PIPE

def get_changed_paths():
    result = run(["git", "diff", "--name-only", "HEAD~1"], stdout=PIPE, text=True, check=True)
    return result.stdout.splitlines()

def get_commit_message(path):
    result = run(["git", "log", "-1", "--pretty=%s", "--", path], stdout=PIPE, text=True)
    return result.stdout.strip()
