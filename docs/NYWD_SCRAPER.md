# NYWD Scraper

The `src/scrapers/nywd_scraper.py` module provides a Playwright-based web scraper for NYWD products.

## Usage

### Import

```python
from src.scrapers.nywd_scraper import NYWDScraper
from playwright.sync_api import sync_playwright
```

### Basic Example

```python
with sync_playwright() as p:
    # Connect to browser via CDP
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = browser.contexts[0].pages[-1]
    
    # Create scraper
    scraper = NYWDScraper(page)
    
    # Scrape a product
    result = scraper.process("583295")
    print(result)
```

## Methods

### search(sku)

Search for a product by SKU.

```python
scraper.search("583295")
```

### has_no_product()

Check if the search returned no results.

```python
if scraper.has_no_product():
    print("Product not found")
```

### open_product(sku)

Open the product detail page.

```python
scraper.open_product("583295")
```

### extract(sku)

Extract product data from the current page.

```python
data = scraper.extract("583295")
```

**Returns:**
```python
{
    "sku": "583295",
    "brand": "Brand Name",
    "name": "Product Name",
    "price": "$99.99",
    "attributes": {
        "Size": "Large",
        "Color": "Blue"
    },
    "images": ["url1", "url2"],
    "url": "https://..."
}
```

### process(sku)

Complete scraping pipeline (search → check → open → extract).

```python
result = scraper.process("583295")
```

**Returns:**
```python
{
    "sku": "583295",
    "status": "found",  # or "not_found"
    "brand": "...",
    "name": "...",
    "price": "...",
    "attributes": {...},
    "images": [...],
    "url": "..."
}
```

## Running the Scraper

### Step 1: Launch Browser with CDP

```bash
# Automatically launched when running the scraper script
python scripts/run_scraper.py
```

Or manually with the launcher:

```python
from src.browser.launcher import launch_brave_browser

launcher = launch_brave_browser()
# ... run scraper ...
launcher.close()
```

### Step 2: Stream Processing

```python
from src.scrapers.nywd_scraper import NYWDScraper
from config.settings import NYWD_DEFAULT_SKUS

skus = ["583295", "583296", "999999"]

for sku in skus:
    result = scraper.process(sku)
    # Process result immediately
    print(result)
```

## Configuration

SKU defaults in `config/settings.py`:

```python
NYWD_DEFAULT_SKUS = ["583295", "583296", "999999"]
```

## Selectors Used

The scraper uses these CSS selectors:

- Search toggle: `#searchToggle`
- Search input: `#searchInput`
- Empty result text: `text=No Product Found`
- Product link: `a[href='/new-product-{sku}']`
- Brand: `h2.font-sans.text-lg`
- Product name: `h2.font-serif.text-3xl`
- Price: `h2.font-serif.text-2xl`
- Attributes: `div.grid.grid-cols-2.lg\:max-w\[400px\]`
- Images: `.swiper-slide img`

## Error Handling

```python
try:
    result = scraper.process(sku)
    if result["status"] == "not_found":
        print(f"SKU {sku} not found")
    else:
        print(f"Scraped {result['name']}")
except Exception as e:
    print(f"Error scraping {sku}: {e}")
```

## Performance Tips

1. **Batch processing**: Process multiple SKUs in one browser session
2. **Timeout handling**: Adjust wait times in `process()` if needed
3. **Error recovery**: Check `has_no_product()` before extracting
4. **Resource cleanup**: Always close the browser after scraping

## Customization

To modify selectors or flow, edit `src/scrapers/nywd_scraper.py`:

```python
def extract(self, sku):
    # Modify selectors here
    brand = self.page.inner_text("h2.YOUR_SELECTOR").strip()
    # ...
```
