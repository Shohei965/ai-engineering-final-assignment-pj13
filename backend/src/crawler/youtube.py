import json
import random
from pathlib import Path
from typing import List

DATA = Path(__file__).resolve().parents[2] / "data" / "sample_youtube.json"


async def search_comments(keywords: List[str], limit: int = 300) -> List[str]:
    """Return random sample YouTube comments."""
    with open(DATA) as f:
        comments = json.load(f)
    random.shuffle(comments)
    return comments[:limit]
    # TODO: Implement real YouTube API search
