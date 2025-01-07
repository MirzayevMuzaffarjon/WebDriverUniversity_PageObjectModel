from Pages.OurProducts import Our_Products

def test_product_page_elemnts_are_visible(page):
    user = Our_Products(page)
    user.product_page_elemnts_are_visible()

def test_actions(page):
    user = Our_Products(page)
    user.actions()