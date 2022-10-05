import feedparser

feed = feedparser.parse('http://rss.art19.com/the-daily')
entries = feed.entries
print(feed.feed.title)
print(len(entries))
for i in range(5):
    print(entries[i].title)
    print(f"Summary: " + entries[i].summary)
    print("Published: " + str(entries[i].published).split(' +')[0])
    print()