import feedparser
import requests

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