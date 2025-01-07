from Pages.ContactUs import Contact_Us

def test_elements_are_visible(page):
    user = Contact_Us(page)
    user.elements_are_visible()

def test_submit_positive_flow(page):
    user = Contact_Us(page)
    user.submit_positive_flow()

def test_reset_form(page):
    user = Contact_Us(page)
    user.reset_form()

def test_submit_with_invalid_email(page):
    user = Contact_Us(page)
    user.submit_with_invalid_email()