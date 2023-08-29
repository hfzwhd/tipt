

import feedparser

url = "https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon=SGR01"
content = feedparser.parse(url)

#print((content).keys())
#print(content.entries)
#print(content.entries[0].title + content.entries[0].summary)
#print(content.feed)

print("\n" + content.feed.updated + " | " + content.feed.subtitle + "\n")

for solat_schedule in content.entries:
    print(solat_schedule.title + ": " + solat_schedule.summary)

print("\nProvider: " + content.feed.author)

