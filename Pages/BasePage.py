from playwright.sync_api import Page

class Base_Page:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url):
        self.page.goto(url, wait_until='load')