import feedparser

# Replace with the URL of the RSS feed you want to access
feed_url = "https://www.theverge.com/apple/rss/index.xml"

# Parse the RSS feed
feed = feedparser.parse(feed_url)

# Check if the feed was parsed successfully
if feed.status != 200:
    print("Error: Failed to fetch feed.")
    exit(1)

# Print the feed title
print(f"Feed Title: {feed.feed.title}")

# Loop through each entry in the feed
for entry in feed.entries:
    print(f"\nTitle: {entry.title}")
    print(f"Link: {entry.link}")

    # print(f"\nSummary: {entry.summary}")

    # Access other elements like published date (parsed format)
    print(f"Published at: {entry.published}")
    print(f"Language: {entry.content[0]['language']}")
    # print(f"{entry.content}")
    # print(f"Updated at: {entry.updated}")
