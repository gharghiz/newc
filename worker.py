import time
from core.scraper import fetch_all_news

while True:
    print("Fetching news...")
    fetch_all_news()
    time.sleep(60)
