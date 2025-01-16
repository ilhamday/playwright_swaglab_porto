class ProductPage:
    
    def __init__(self,page):
        self.page = page

    def check_title_text(self):
        text = self.page.locator("//div[@class='app_logo']").text_content()
        return text
