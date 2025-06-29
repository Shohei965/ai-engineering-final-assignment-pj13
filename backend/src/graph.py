import asyncio
from collections import Counter

from .crawler import reddit, twitter, youtube
from .llm.gemini import llm_analyze


async def collect_posts(keywords: list[str]) -> list[str]:
    tasks = [
        twitter.search_tweets(keywords),
        reddit.search_posts(keywords),
        youtube.search_comments(keywords),
    ]
    results = await asyncio.gather(*tasks)
    posts: list[str] = []
    for r in results:
        posts.extend(r)
    return posts


async def sentiment_and_keywords(posts: list[str]) -> list[dict]:
    return await llm_analyze(posts)


async def aggregate_results(analyses: list[dict]) -> dict:
    pos = sum(1 for a in analyses if a.get("sentiment") == "pos")
    neg = sum(1 for a in analyses if a.get("sentiment") == "neg")
    keywords = [kw for a in analyses for kw in a.get("keywords", [])]
    freq = Counter(keywords)
    top_words = freq.most_common(20)
    summary = {
        "summary": f"Positive {pos} / Negative {neg}",
        "pos_count": pos,
        "neg_count": neg,
        "word_freq": dict(top_words),
        "samples": analyses[:5],
    }
    return summary


async def runner(keywords: list[str]) -> dict:
    posts = await collect_posts(keywords)
    analyses = await sentiment_and_keywords(posts)
    return await aggregate_results(analyses)
