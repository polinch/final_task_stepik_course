import pytest

from faker import Faker
from faker.providers import internet

from random import random

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.links import Links


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [f"{product_base_link}?promo=offer{no}" if no != 7
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.login
class TestLoginFromProductPage:
    def test_user_can_go_to_login_page(self, browser):
        link = Links.PRODUCT_PAGE_LINK
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_user_should_see_login_link(self, browser):
        link = Links.PRODUCT_PAGE_LINK
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # prepare fake data
        fake = Faker()
        Faker.seed(random())
        fake.add_provider(internet)
        test_email = fake.email()
        test_password = fake.password()

        link = Links.LOGIN_PAGE_LINK
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(test_email, test_password)
        browser.implicitly_wait(15)
        login_page.should_be_authorized_user()

    def test_guest_can_add_product_to_basket(self, browser):
        link = Links.PRODUCT_PAGE_LINK
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        link = Links.PRODUCT_PAGE_LINK
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Links.PRODUCT_PAGE_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = Links.PRODUCT_PAGE_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Links.PRODUCT_PAGE_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_disappear_success_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Links.PRODUCT_PAGE_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
