import feedparser
from project_config import RSS_FEEDS, KEYWORDS

def fetch_articles():
    articles = []
    for url in RSS_FEEDS:
        print(f"📥 正在读取 RSS: {url}")
        feed = feedparser.parse(url)
        print(f"📦 共获取 {len(feed.entries)} 条记录")
        for entry in feed.entries:
            content = entry.title + entry.summary
            if any(keyword in content for keyword in KEYWORDS):
                articles.append({
                    "title": entry.title,
                    "summary": entry.summary,
                    "link": entry.link
                })
                print(f"✅ 匹配文章：{entry.title}")
            else:
                print(f"❌ 跳过：{entry.title}")
    return articles

# ✅ 测试代码
if __name__ == "__main__":
    articles = fetch_articles()
    print(f"\n📊 最终匹配到 {len(articles)} 篇文章")
    for article in articles:
        print("📄 标题:", article["title"])
        print("🧾 摘要:", article["summary"])
        print("🔗 链接:", article["link"])
        print("-" * 60)
