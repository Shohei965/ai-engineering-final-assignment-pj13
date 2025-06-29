import json
import random
from pathlib import Path
from typing import List

DATA = Path(__file__).resolve().parents[2] / "data" / "sample_tweets.json"


async def search_tweets(keywords: List[str], limit: int = 300) -> List[str]:
    """Return random sample tweets."""
    with open(DATA) as f:
        tweets = json.load(f)
    random.shuffle(tweets)
    return tweets[:limit]
    # TODO: Implement real Twitter API search
