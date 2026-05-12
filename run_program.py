from playwright.sync_api import sync_playwright
from src.scrapers.nywd_scraper import NYWDScraper
from src.browser.launcher import launch_brave_browser
from config.settings import NYWD_DEFAULT_SKUS
import json

SKUS = NYWD_DEFAULT_SKUS

def stream_scrape(scraper, skus):

    for sku in skus:

        print(f"\nProcessing SKU: {sku}")

        result = scraper.process(sku)

        # 🔥 STREAM OUTPUT IMMEDIATELY
        yield result


with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = browser.contexts[0].pages[-1]

    scraper = NYWDScraper(page)

    # consume stream
    for result in stream_scrape(scraper, SKUS):

        print("\nSTREAMED RESULT:")
        print(json.dumps(result, indent=4))