from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator('[data-test="inventory-item"]')
        self.checkout_btn = page.locator('[data-test="checkout"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_btn = page.locator('[data-test="continue"]')
        self.finish_btn = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('[data-test="complete-header"]')

    def start_checkout(self):
        self.checkout_btn.click()

    def fill_details(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_btn.click()

    def finish(self):
        self.finish_btn.click()