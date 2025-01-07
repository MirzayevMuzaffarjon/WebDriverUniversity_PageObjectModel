from Pages.HomePage import Home_Page

def test_home_page_elements_are_visible(page):
    user = Home_Page(page)
    user.home_page_elements_are_visible()

def test_button_actions(page):
    user = Home_Page(page)
    user.button_actions()

def test_carousel(page):
    user = Home_Page(page)
    user.carousel()