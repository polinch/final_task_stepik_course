import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.links import Links


@pytest.mark.login
class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = Links.MAIN_PAGE_LINK
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = Links.MAIN_PAGE_LINK
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = Links.MAIN_PAGE_LINK
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
