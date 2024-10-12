from playwright.sync_api import Page, expect
import pytest

def test_login_valid_cret(page: Page):
    page.goto("https://www.saucedemo.com/")

    field_usr = page.get_by_placeholder("Username")
    field_pass = page.get_by_placeholder("Password")
    # btn_login = page.get_by_role("submit", name="login-button")
    btn_login = page.locator("//input[@id='login-button']")

    field_usr.fill("standard_user")
    field_pass.fill("secret_sauce")
    btn_login.click()

    
    expect(page.get_by_test_id("shopping_cart_container")).to_be_visible
    expect(page).to_have_title("Swag Labs")

# def test_product_to_cart(page: Page):
    # page.goto("https://www.saucedemo.com/inventory.html") # Masih butuh goto terus.

    # get the first add to card button
    # btn_add_to_cart = page.get_by_role("button", name="Add to cart") #this doens't works
    btn_add_to_cart = page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")

    btn_add_to_cart.click() 

    expect(page.locator("//*[@id='shopping_cart_container']/a/span")).to_be_visible

    
    #Go to Cart Page
    # btn_cart = page.get_by_test_id("shopping_cart_container")
    btn_cart = page.locator("//*[@id='shopping_cart_container']/a")
    btn_cart.click()

    expect(page.get_by_role("span", name="Your Cart")).to_be_visible
    expect(page.get_by_test_id("continue-shopping")).to_be_visible

    #Process checkout
    btn_checkout = page.get_by_role("button", name="Checkout")
    btn_checkout.click()

    expect(page.get_by_role("span", name="Checkout: Your Information")).to_be_visible
    expect(page.get_by_test_id("first-name")).to_be_visible
    expect(page.get_by_test_id("last-name")).to_be_visible