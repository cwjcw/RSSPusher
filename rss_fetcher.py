import feedparser
from config import RSS_FEEDS, KEYWORDS

def fetch_articles():
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            content = entry.title + entry.summary
            if any(keyword in content for keyword in KEYWORDS):
                articles.append({
                    "title": entry.title,
                    "summary": entry.summary,
                    "link": entry.link
                })
    return articles
