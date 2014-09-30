def feed():
    import feedparser
    d = feedparser.parse('http://www.reddit.com/r/python/.rss')
    entries = d.entries
    return dict(message=sif, source=source, title1=title1, entries=entries)
