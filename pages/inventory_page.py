from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.prices = page.locator('[data-test="inventory-item-price"]')
        self.names = page.locator('[data-test="inventory-item-name"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def add_to_cart(self, slug: str):
        # slug example: "sauce-labs-backpack"
        self.page.get_by_test_id(f"add-to-cart-{slug}").click()

    def sort_by(self, value: str):
        # values: az, za, lohi, hilo
        self.sort_dropdown.select_option(value)

    def get_prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def get_names(self) -> list[str]:
        return self.names.all_inner_texts()

    def open_cart(self):
        self.cart_link.click()