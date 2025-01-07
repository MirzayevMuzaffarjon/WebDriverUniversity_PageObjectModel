from Pages.BasePage import Base_Page
from playwright.sync_api import expect

class Our_Products(Base_Page):
    def __init__(self, page):
        super().__init__(page)

    def product_page_elemnts_are_visible(self):
        self.go_to("https://webdriveruniversity.com/Page-Object-Model/products.html")

        expect(self.page.get_by_role("link", name="Home")).to_be_visible()
        expect(self.page.get_by_role("link", name="Our Products")).to_be_visible()
        expect(self.page.get_by_role("link", name="Contact Us")).to_be_visible()

        product_count = self.page.locator('//div[@class="thumbnail"]').count()
        for i in range(product_count):
            expect(self.page.locator('//div[@class="thumbnail"]').nth(i)).to_be_visible()

    def actions(self):
        self.go_to("https://webdriveruniversity.com/Page-Object-Model/products.html")

        product_count = self.page.locator('//div[@class="thumbnail"]').count()
        for i in range(product_count):
            self.page.locator('//div[@class="thumbnail"]').nth(i).click()
            expect(self.page.get_by_text("SPECIAL OFFER!")).to_be_visible()
            expect(self.page.get_by_role("button", name="×")).to_be_visible()
            expect(self.page.get_by_role("button", name="Proceed")).to_be_visible()
            expect(self.page.get_by_role("button", name="Close")).to_be_visible()
            self.page.get_by_role("button", name="×").click()

            self.page.locator('//div[@class="thumbnail"]').nth(i).click()
            expect(self.page.get_by_text("SPECIAL OFFER!")).to_be_visible()
            expect(self.page.get_by_role("button", name="×")).to_be_visible()
            expect(self.page.get_by_role("button", name="Proceed")).to_be_visible()
            expect(self.page.get_by_role("button", name="Close")).to_be_visible()
            self.page.get_by_role("button", name="Proceed").click()

            self.page.locator('//div[@class="thumbnail"]').nth(i).click()
            expect(self.page.get_by_text("SPECIAL OFFER!")).to_be_visible()
            expect(self.page.get_by_role("button", name="×")).to_be_visible()
            expect(self.page.get_by_role("button", name="Proceed")).to_be_visible()
            expect(self.page.get_by_role("button", name="Close")).to_be_visible()
            self.page.get_by_role("button", name="Close").click()