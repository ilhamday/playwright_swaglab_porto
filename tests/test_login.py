from playwright.sync_api import Page, expect
import pytest

from pages.login import LoginPage # We can use * (start sign)
from pages.product import ProductPage

@pytest.fixture
def browser(page: Page):
    page.set_viewport_size({"width":1920, "height":1080})
    yield page
    page.close()

def test_login(browser):
    login = LoginPage(browser) # Create login as object
    product = ProductPage(browser)

    browser.goto("https://saucedemo.com")

    login.input_username()
    login.input_password()
    login.click_login_btn()

    product_page_title = product.check_title_text()
    assert product_page_title == "Swag Labs"

