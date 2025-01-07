from Pages.BasePage import Base_Page
from playwright.sync_api import expect

class Contact_Us(Base_Page):
    def __init__(self, page):
        super().__init__(page)

    def elements_are_visible(self):
        self.go_to("https://webdriveruniversity.com/Contact-Us/contactus.html")

        expect(self.page.get_by_role("heading", name="CONTACT US")).to_be_visible()
        expect(self.page.get_by_placeholder("First Name")).to_be_visible()
        expect(self.page.get_by_placeholder("Last Name")).to_be_visible()
        expect(self.page.get_by_placeholder("Email Address")).to_be_visible()
        expect(self.page.get_by_placeholder("Comments")).to_be_visible()
        expect(self.page.get_by_role("button", name="RESET")).to_be_visible()
        expect(self.page.get_by_role("button", name="SUBMIT")).to_be_visible()

    def submit_positive_flow(self):
        self.go_to("https://webdriveruniversity.com/Contact-Us/contactus.html")

        self.page.get_by_placeholder("First Name").click()
        self.page.get_by_placeholder("First Name").fill("Test First Name")
        self.page.get_by_placeholder("Last Name").click()
        self.page.get_by_placeholder("Last Name").fill("Test Last Name")
        self.page.get_by_placeholder("Email Address").click()
        self.page.get_by_placeholder("Email Address").fill("emailaddress@gmail.com")
        self.page.get_by_placeholder("Comments").click()
        self.page.get_by_placeholder("Comments").fill("test comments test comments test comments test comments")
        self.page.get_by_role("button", name="SUBMIT").click()
        expect(self.page.get_by_role("heading", name="Thank You for your Message!")).to_be_visible()
        expect(self.page.locator("#fountainG")).to_be_visible()

    def reset_form(self):
        self.go_to("https://webdriveruniversity.com/Contact-Us/contactus.html")

        self.page.get_by_placeholder("First Name").click()
        self.page.get_by_placeholder("First Name").fill("Test First Name")
        self.page.get_by_placeholder("Last Name").click()
        self.page.get_by_placeholder("Last Name").fill("Test Last Name")
        self.page.get_by_placeholder("Email Address").click()
        self.page.get_by_placeholder("Email Address").fill("emailaddress@gmail.com")
        self.page.get_by_placeholder("Comments").click()
        self.page.get_by_placeholder("Comments").fill("test comments test comments test comments test comments")
        self.page.get_by_role("button", name="RESET").click()

        name_input_value = self.page.get_by_placeholder("First Name").input_value()
        assert name_input_value == ""

        name_input_value = self.page.get_by_placeholder("Last Name").input_value()
        assert name_input_value == ""

        name_input_value = self.page.get_by_placeholder("Email Address").input_value()
        assert name_input_value == ""

        name_input_value = self.page.get_by_placeholder("Comments").input_value()
        assert name_input_value == ""

    def submit_with_invalid_email(self):
        self.go_to("https://webdriveruniversity.com/Contact-Us/contactus.html")

        self.page.get_by_placeholder("First Name").click()
        self.page.get_by_placeholder("First Name").fill("Test First Name")
        self.page.get_by_placeholder("Last Name").click()
        self.page.get_by_placeholder("Last Name").fill("Test Last Name")
        self.page.get_by_placeholder("Email Address").click()
        self.page.get_by_placeholder("Email Address").fill("test")
        self.page.get_by_placeholder("Comments").click()
        self.page.get_by_placeholder("Comments").fill("test comments test comments test comments test comments")
        self.page.get_by_role("button", name="SUBMIT").click()
        expect(self.page.get_by_text("Error: Invalid email address")).to_be_visible()







