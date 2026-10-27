import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.ui
def test_end_to_end_purchase(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    inv.open_cart()

    checkout = CheckoutPage(logged_in_page)
    expect(checkout.cart_items).to_have_count(1)
    checkout.start_checkout()
    checkout.fill_details("Sasanka", "Posina", "560001")
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")