from pathlib import Path

VERSION_FILE = Path("version.txt")


def get_version() -> str:
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()
    return "0.1.0"
