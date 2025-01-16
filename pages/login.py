class LoginPage:

    def __init__(self,page):
        self.page = page

    def input_username(self):
        field_usr = self.page.get_by_placeholder("Username")
        field_usr.fill("standard_user")

    def input_password(self):
        field_pass = self.page.get_by_placeholder("Password")
        field_pass.fill("secret_sauce")

    def click_login_btn(self):
        btn_login = self.page.locator("//input[@id='login-button']")  
        btn_login.click()