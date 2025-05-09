from rss_fetcher import fetch_articles
from content_processor import summarize_article
from wechat_pusher import push_to_wechat

def run():
    articles = fetch_articles()
    for article in articles:
        summary = summarize_article(article["summary"])
        push_to_wechat(article["title"], article["link"], summary)

if __name__ == "__main__":
    run()
