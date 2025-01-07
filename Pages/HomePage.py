from Pages.BasePage import Base_Page
from playwright.sync_api import expect

class Home_Page(Base_Page):
    def __init__(self, page):
        super().__init__(page)

    def home_page_elements_are_visible(self):
        self.page.goto("https://webdriveruniversity.com/Page-Object-Model/index.html", wait_until='load')
        expect(self.page.get_by_role("link", name="WebdriverUniversity.com (Page Object Model)")).to_be_visible()
        expect(self.page.locator("#carousel-example-generic")).to_be_visible()
        expect(self.page.get_by_role("link", name="Home")).to_be_visible()
        expect(self.page.get_by_role("link", name="Our Products")).to_be_visible()
        expect(self.page.get_by_role("link", name="Contact Us")).to_be_visible()
        expect(self.page.get_by_text("Who Are We?")).to_be_visible()
        expect(self.page.get_by_text("GREAT SERVICE!")).to_be_visible()
        self.page.get_by_text("Why Choose Us?").scroll_into_view_if_needed()
        expect(self.page.get_by_text("Why Choose Us?")).to_be_visible()
        expect(self.page.get_by_text("Excellent Customer Service!")).to_be_visible()

    def click_find_out_more(self):
        self.page.get_by_role("button", name="Find Out More!").click()

        # Assertions to validate modal visibility
        expect(self.page.get_by_role("heading", name="Welcome to")).to_be_visible()
        expect(self.page.get_by_role("button", name="×")).to_be_visible()
        expect(self.page.get_by_role("button", name="Find Out More", exact=True)).to_be_visible()
        expect(self.page.get_by_role("button", name="Close")).to_be_visible()

    def button_actions(self):
        self.page.goto("https://webdriveruniversity.com/Page-Object-Model/index.html", wait_until='load')
        self.page.get_by_role("button", name="Find Out More!").scroll_into_view_if_needed()

        # Testing button actions
        self.click_find_out_more()
        self.page.get_by_role("button", name="Find Out More", exact=True).click()

        self.click_find_out_more()
        self.page.get_by_role("button", name="Close").click()

        self.click_find_out_more()
        self.page.get_by_role("button", name="×").click()

    def carousel(self):
        self.page.goto("https://webdriveruniversity.com/Page-Object-Model/index.html", wait_until='load')

        # Verify all carousel images are visible
        images_count = self.page.locator("//img[@class='slide-image']").count()

        for i in range(images_count):
            expect(self.page.locator("//img[@class='slide-image']").nth(i)).to_be_visible(timeout=7500)

        self.page.reload()

        # Navigate carousel using arrows
        for i in range(images_count):
            expect(self.page.locator("//img[@class='slide-image']").nth(i)).to_be_visible()
            self.page.wait_for_timeout(600)
            self.page.locator('//span[@class="glyphicon glyphicon-chevron-right"]').click()

        self.page.reload()

        # Interact with carousel indicators
        indicators_count = self.page.locator('//li[@data-target="#carousel-example-generic"]').count()

        for i in range(indicators_count):
            expect(self.page.locator("//img[@class='slide-image']").nth(i)).to_be_visible()
            self.page.wait_for_timeout(600)
            if i == indicators_count-1:
                break
            else:
                self.page.locator('//li[@data-target="#carousel-example-generic"]').nth(i+1).click()