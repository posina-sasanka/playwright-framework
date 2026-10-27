import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(InventoryPage(page).title).to_have_text("Products")


#@pytest.mark.ui
# @pytest.mark.parametrize(
#     "user,pwd,message",
#     [
#         ("locked_out_user", "secret_sauce", "locked out"),
#         ("standard_user", "wrong_pass", "do not match"),
#         ("", "secret_sauce", "Username is required"),
#         ("standard_user", "", "Password is required"),
#     ],
# )
# def test_invalid_login(page, user, pwd, message):
#     login = LoginPage(page)
#     login.open()
#     login.login(user, pwd)
#     expect(login.error).to_contain_text(message)