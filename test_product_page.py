from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
