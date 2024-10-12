from playwright.sync_api import sync_playwright, expect

def test_login_valid_cret(page):
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

def test_product_to_cart(page):
    # page.goto("https://www.saucedemo.com/inventory.html")
    # get the first add to card button
    btn_add_to_cart = page.get_by_role("button", name="Add to cart")
    # btn_add_to_cart = page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")

    btn_add_to_cart.click()

    expect(page.locator("//*[@id='shopping_cart_container']/a/span")).to_be_visible

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

    page = test_login_valid_cret(page)
    page = test_product_to_cart(page)

    # Close the browser
    browser.close()

if __name__ == "__main__":
    main()