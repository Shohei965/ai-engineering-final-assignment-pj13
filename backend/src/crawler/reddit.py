import json
import random
from pathlib import Path
from typing import List

DATA = Path(__file__).resolve().parents[2] / "data" / "sample_reddit.json"


async def search_posts(keywords: List[str], limit: int = 300) -> List[str]:
    """Return random sample reddit posts."""
    with open(DATA) as f:
        posts = json.load(f)
    random.shuffle(posts)
    return posts[:limit]
    # TODO: Implement real Reddit API search
