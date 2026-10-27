import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_sort_price_low_to_high(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("lohi")
    prices = inv.get_prices()
    assert prices == sorted(prices)


@pytest.mark.ui
def test_sort_name_z_to_a(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.sort_by("za")
    names = inv.get_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.ui
def test_cart_badge_count(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    inv.add_to_cart("sauce-labs-bike-light")
    expect(inv.cart_badge).to_have_text("2")