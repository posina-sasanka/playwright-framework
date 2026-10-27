import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("link", name="Playwright logo Playwright")).to_be_visible()
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
