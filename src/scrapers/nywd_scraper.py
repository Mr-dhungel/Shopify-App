class NYWDScraper:
    """NYWD Product Scraper using Playwright"""

    def __init__(self, page):
        self.page = page

    # -------------------------
    # SEARCH SKU
    # -------------------------
    def search(self, sku):
        """Search for a product by SKU"""
        self.page.click("#searchToggle")
        self.page.wait_for_selector("#searchInput")

        self.page.fill("#searchInput", sku)
        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(3000)

    # -------------------------
    # CHECK EMPTY RESULT
    # -------------------------
    def has_no_product(self):
        """Check if search returned no products"""
        return self.page.locator("text=No Product Found").count() > 0

    # -------------------------
    # OPEN PRODUCT
    # -------------------------
    def open_product(self, sku):
        """Open a product detail page"""
        try:
            self.page.click(f"a[href='/new-product-{sku}']")
        except:
            self.page.click("#product-detail-image1")

        self.page.wait_for_timeout(3000)

    # -------------------------
    # EXTRACT DATA
    # -------------------------
    def extract(self, sku):
        """Extract product data from page"""

        brand = self.page.inner_text("h2.font-sans.text-lg").strip()
        name = self.page.inner_text("h2.font-serif.text-3xl").strip()
        price = self.page.inner_text("h2.font-serif.text-2xl").strip()

        labels = self.page.locator(
            "div.grid.grid-cols-2.lg\\:max-w\\[400px\\] > div:nth-child(odd)"
        )
        values = self.page.locator(
            "div.grid.grid-cols-2.lg\\:max-w\\[400px\\] > div:nth-child(even)"
        )

        attributes = {}

        for i in range(labels.count()):
            key = labels.nth(i).inner_text().strip().replace(":", "")
            value = values.nth(i).inner_text().strip()
            attributes[key] = value

        images = self.page.eval_on_selector_all(
            ".swiper-slide img", "imgs => imgs.map(i => i.src)"
        )

        return {
            "sku": sku,
            "brand": brand,
            "name": name,
            "price": price,
            "attributes": attributes,
            "images": images,
            "url": self.page.url,
        }

    # -------------------------
    # FULL PIPELINE
    # -------------------------
    def process(self, sku):
        """Full scraping pipeline for a single SKU"""

        self.search(sku)

        if self.has_no_product():
            return {
                "sku": sku,
                "status": "not_found",
                "brand": None,
                "name": None,
                "price": None,
                "attributes": {},
                "images": [],
                "url": self.page.url,
            }

        self.open_product(sku)

        data = self.extract(sku)
        data["status"] = "found"

        return data
