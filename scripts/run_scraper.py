#!/usr/bin/env python
"""
Script to run the NYWD scraper.

Usage:
    python scripts/run_scraper.py
"""

from playwright.sync_api import sync_playwright
from src.scrapers.nywd_scraper import NYWDScraper
from src.browser.launcher import launch_brave_browser
from config.settings import NYWD_DEFAULT_SKUS
import json


def stream_scrape(scraper, skus):
    """Stream scrape results for multiple SKUs"""
    for sku in skus:
        print(f"\nProcessing SKU: {sku}")
        result = scraper.process(sku)
        yield result


def main(skus: list = None):
    """Main scraper entry point"""
    skus = skus or NYWD_DEFAULT_SKUS

    # Launch Brave browser with remote debugging
    launcher = launch_brave_browser()

    try:
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
            page = browser.contexts[0].pages[-1]

            scraper = NYWDScraper(page)

            # Consume stream and print results
            for result in stream_scrape(scraper, skus):
                print("\nSTREAMED RESULT:")
                print(json.dumps(result, indent=4))

    finally:
        launcher.close()


if __name__ == "__main__":
    main()
