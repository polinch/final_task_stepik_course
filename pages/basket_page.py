from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Message \'Empty basket\' should be on this page"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Basket should be empty"

    def should_be_empty_basket(self):
        self.should_not_be_product_in_basket()
        self.should_be_empty_basket_message()
