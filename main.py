import feedparser
import requests

# is_https = "https://" in 'https://news.google.com/news?ned=us&output=rss'[:len("https://")]
# if is_https:
#   feed_content = requests.get('https://news.google.com/news?ned=us&output=rss')
#   feed = feedparser.parse(feed_content.text)
# elif not is_https:
#   feed = feedparser.parse('https://news.google.com/news?ned=us&output=rss')

feed_content = requests.get('http://rss.art19.com/the-daily')
feed = feedparser.parse(feed_content.text)
entries = feed.entries
print(feed.feed.title)
print(len(entries))
for i in range(5):
    print(entries[i].title)
    print(f"Summary: " + entries[i].summary)
    print(f"Published: {str(entries[i].published).split(' +')[0]}")
    print()