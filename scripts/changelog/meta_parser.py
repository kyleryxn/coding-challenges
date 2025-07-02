import json
from pathlib import Path


def parse_topics_from_meta(file_path: str):
    parts = Path(file_path).parts
    if len(parts) < 2 or parts[0] != "challenges":
        return []

    challenge_dir = Path("challenges") / parts[1]
    meta_path = challenge_dir / "meta.json"
    if meta_path.exists():
        try:
            with open(meta_path, "r") as f:
                meta = json.load(f)
            return meta.get("topics", [])
        except Exception:
            return []
    return []
