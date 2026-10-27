import pytest
from pages.login_page import LoginPage
from utils.config import API_URL, API_USER, API_PASS, USERNAME, PASSWORD


@pytest.fixture(scope="session", autouse=True)
def _use_data_test_attribute(playwright):
    # saucedemo uses data-test instead of Playwright's default data-testid
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1366, "height": 768}}


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    return page


@pytest.fixture(scope="session")
def api_context(playwright):
    ctx = playwright.request.new_context(
        base_url=API_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    yield ctx
    ctx.dispose()


@pytest.fixture(scope="session")
def auth_token(api_context):
    resp = api_context.post("/auth", data={"username": API_USER, "password": API_PASS})
    assert resp.ok
    return resp.json()["token"]